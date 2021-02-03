import os
import requests
import gzip
import shutil
import json
from itertools import islice

def download(url, file):
  r = requests.get(url, allow_redirects=True)
  open(file, 'wb').write(r.content)

def ungzip(file):
  outfile = file.replace('.gz', '')
  with gzip.open(file, 'rb') as f_in:
    with open(outfile, 'wb') as f_out:
        shutil.copyfileobj(f_in, f_out)

  os.remove(file)
  return outfile

def get_jsonline(url):
  file = os.path.join(DATA_PATH, os.path.basename(url))
  download(url, file)
  return ungzip(file)

def file_len(fname):
    with open(fname) as f:
        for i, _ in enumerate(f):
            pass
    return i + 1

def word_count(text):
  from collections import Counter
  import re
  words = re.findall(r'\w+', text.lower())
  return Counter(words)

def divide_train(file, name1, name2):
  lineas = file_len(file)
  break_line = int(lineas * .8)
  smallfile = None
  small_filename = "{0}.jl".format(name1)
  smallfile = open(small_filename, "w")
  with open(file) as bigfile:
    for lineno, line in enumerate(bigfile):
        if lineno  == break_line:
            if smallfile:
                smallfile.close()
            small_filename = "{0}.jl".format(name2)
            smallfile = open(small_filename, "w")
        smallfile.write(line)
    if smallfile:
        smallfile.close()

  return(("{0}.jl".format(name1), "{0}.jl".format(name2)))

def create_data_from_urls(urlitems, urltrain, urltest):

  items_data = {}
  train_data = {}
  test_data = {}

  file = get_jsonline(urlitems)
  with open(file) as bigfile:
    for line in bigfile:
        data = json.loads(line)
        try:
          itemkey = data.get('item_id',-1)
          text = " ".join([str(itemkey),
                           data.get('title',''),
                           '' if data['domain_id'] is None else data.get('domain_id',''),
                           data.get('category_id','')])
          items_data[itemkey] = text

        except TypeError:
          print(data)
          raise

  os.remove(file)

  n = 1
  file = get_jsonline(urltest)
  with open(file) as bigfile:
    for line in bigfile:
      data = json.loads(line)
      text = ""
      for e in data['user_history']:
          item_or_search =  e.get('event_info', "")
          if e['event_type'] == 'view':
            text = text + " " + items_data.get(int(item_or_search), "")
          else:
            text = text + " " + item_or_search

      test_data[n] = word_count(text)
      n = n + 1

  os.remove(file)


  file = get_jsonline(urltrain)
  with open(file) as bigfile:
    for line in bigfile:
      data = json.loads(line)
      text = ""
      itemkey = data.get('item_bought',-1)
      for e in data['user_history']:
          item_or_search =  e.get('event_info', "")
          if e['event_type'] == 'view':

            text = text + " " + items_data.get(int(item_or_search), "")
          else:
            text = text + " " + data.get('event_info', "")

      train_data[itemkey] = word_count(text)

  for k, text in items_data.items():
    if k not in train_data:
      train_data[k] = word_count(text)

  os.remove(file)

  return (train_data, test_data)

def obj_to_pickle(obj, file):
  import pickle
  with open(file, 'wb') as handle:
    pickle.dump(obj, handle, protocol=pickle.HIGHEST_PROTOCOL)

def pickle_to_obj(path):
    with open(path, 'rb') as handle:
        return pickle.load(handle)

def take(n, iterable):
    "Return first n items of the iterable as a list"
    return list(islice(iterable, n))

def top_n(d, n):
  l = [(k,e) for k, e in sorted(d.items(), key=lambda item: item[1], reverse=True)][0:10]
  return dict(l)


def setup():

    training_data, test_data = create_data_from_urls(
                            urlitems = 'https://meli-data-challenge.s3.amazonaws.com/2020/item_data.jl.gz',
                            urltrain = 'https://meli-data-challenge.s3.amazonaws.com/2020/train_dataset.jl.gz',
                            urltest = 'https://meli-data-challenge.s3.amazonaws.com/2020/test_dataset.jl.gz'
                            )

    corpus_words = {}
    for k, v in training_data.items():
        for word in v:
            if word not in corpus_words:
                corpus_words[word] = 1
            else:
                corpus_words[word] += v[word]

    for k, v in training_data.items():
        for word in v:
             v[word] = v[word] / corpus_words[word]
        training_data[k] = top_n(v, 10)


    obj_to_pickle(training_data, os.path.join(DATA_PATH, "train_data.pickle"))
    obj_to_pickle(test_data, os.path.join(DATA_PATH, "test_data.pickle"))
    obj_to_pickle(corpus_words, os.path.join(DATA_PATH, 'corpus_words.pickle'))

def posibles(test_item, corpus_words, training_data):

  posibles = []
  for test_word, test_wordcount in test_item.items():
    for train_item, train_counter in take(100000,training_data.items()):
      puntaje = 0
      for train_word, train_counter in train_counter.items():
        if test_word == train_word:
          puntaje += train_counter[train_word]

      posibles.append((train_item, puntaje))

  return [i for i, p in sorted(posibles, key=lambda tup: tup[1], reverse=True)[0:10]]

DATA_PATH = '.'

training_data = pickle_to_obj(os.path.join(DATA_PATH, 'train_data.pickle'))
test_data = pickle_to_obj(os.path.join(DATA_PATH, 'test_data.pickle'))

import random , os
import multiprocessing as mp
from queue import Empty
import math
import time
import timeit
from pprint import pprint


pprint(type(test_data))
casos = take(10,test_data.items())


posibles = []
posibles = [posibles(i) for i in casos]

"""
print('Time to execute as a single process: ', end='')
timeit.timeit('[puntaje(i) for i in y]', number = 1, globals=globals())
print('')

posibles = []
p=mp.Pool(8)
p.map(puntaje,y)
"""