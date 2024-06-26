import csv
import pprint

pp = pprint.PrettyPrinter(width=132, compact=True)

training_data = []
corpus_words = {}
classes = {True: [], False: []}

# Lectura del CSV de entrenamiento
with open("train.csv", encoding="utf-8") as csvfile:
	reader = csv.reader(csvfile, delimiter=",")
	for row in reader:
		training_data.append({"me_interesa": True if row[1].strip() == "1" else False, "titulo": row[0]})

# Vamos a imprimir los titulos que me interesan
print("Estos son los titulos de entrenamiento ---------------------------")
pp.pprint(training_data)
pp.pprint([t["titulo"] for t in training_data if t["me_interesa"]])

# Entrenamiento del algoritmo
for data in training_data:
	# Convierto cada titulo en una lista de tokens, elimino algunos innecesarios
	for word in [word for word in data['titulo'].split() if word not in [',', ';', '+', '-', '=', ' ']]:
		if word not in corpus_words:
			corpus_words[word] = 1
		else:
			corpus_words[word] += 1

		# agrego el word a la lista de classes
		classes[data['me_interesa']].extend([word])

print("Este es el corpus ------------------------------------------------")
pp.pprint(corpus_words)
print("Estas son las clases y la lista palabras asociadas ---------------")
pp.pprint(classes)


def puntaje(titulo, clase):
	puntaje = 0.0
	for word in [word for word in titulo.split() if word not in [',', ';', '+', '-', '=', ' ']]:

		if word in classes[clase]:
			puntaje += (1.0 / corpus_words[word])

	return puntaje
	
	
	# Probar el algoritmo
titulos_prueba = ["Data Science in Python: Pandas Cheat Sheet",
				  "Deep Learning for Chess using Theano",
				  "Distributing a script on windows is surprisingly challenging."]

for t in titulos_prueba:
	print("El titulo {0} tiene un puntaje de {1} para la clase 'Me interesa'".format(t, puntaje(t, True)))
	print("El titulo {0} tiene un puntaje de {1} para la clase 'No me interesa'".format(t, puntaje(t, False)))
