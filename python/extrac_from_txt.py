import re
import glob
import csv

paises = "Brasil|Italia|España"
regex = r"PU.(\d+).*Alta (\d{2}:\d{2})hs.*(" + paises +")|PU.(\d+).*Alta (\d{2}:\d{2})hs.*"

def extract_patterns(txt, regex):
 
  matches = re.finditer(regex, txt, re.MULTILINE)
  casos = []
  for matchNum, match in enumerate(matches, start=1):
      if match.group(1) is None:
        casos.append((match.group(4), match.group(5), None))
      else:
        casos.append((match.group(1), match.group(2), match.group(3)))
     
  return(casos)

if __name__ == "__main__":

  resultados = []
  for file in glob.glob("*.txt"):
    with open(file) as f:
       txt = f.read()
       item = [ (file, tupla[0], tupla[1], tupla[2]) for tupla in extract_patterns(txt, regex)]
       resultados = resultados + item
 
  with open('resultados.csv','wt') as out:
    csv_out=csv.writer(out)
    csv_out.writerow(['documento','PU', 'Alta', 'Pais'])
    for row in resultados:
        csv_out.writerow(row)