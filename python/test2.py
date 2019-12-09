from nltk.corpus import stopwords
stop_words = (stopwords.words("spanish"))
print repr(stop_words)
stop_words = [sw.encode('ascii','ignore').decode('UTF8') for sw in stop_words]
print repr(stop_words)

