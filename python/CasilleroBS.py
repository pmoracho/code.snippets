from string import ascii_uppercase
import itertools
import pprint


class Casillero():

	@staticmethod
	def create_casillero(cantidad):

		def iter_all_letters():
			size = 1
			while True:
				for s in itertools.product(ascii_uppercase, repeat=size):
					yield "".join(s)
					size += 1

		letras = [l for l in itertools.islice(iter_all_letters(), cantidad)]
		numeros = [str(n) for n in range(1, cantidad+1)]
		coordenadas = ["{0}{1}".format(l, n) for l, n in itertools.product(letras, numeros)]

		return zip(*[coordenadas[x:x+cantidad] for x in range(0, len(coordenadas), cantidad)])

	def __init__(self, cantidad):

		self.casillero = self.create_casillero(cantidad)
		self._dict_casillero = {key: value for (key, value) in [(c, (fi, ci)) for fi, f in enumerate(self.casillero) for ci, c in enumerate(f)]}
		self._dict_casillero_inv = {v: k for k, v in self._dict_casillero.items()}

	def posibles(self, coordenada):

		f, c = self._dict_casillero[coordenada]
		p = [(f, c+1), (f, c-1), (f-1, c), (f+1, c)]

		return [self._dict_casillero_inv.get(d) for d in p if d in self._dict_casillero_inv]


c = Casillero(10)

pprint.pprint(c.casillero)
print(c.posibles("A3"))
