from PIL import Image

imagen = Image.open("/home/pmoracho/Escritorio/fin.curso/DSC_2528.JPG")
print ('tamaño: ' + str(imagen.size))

ancho = int(imagen.size[0]/13)
alto = int(imagen.size[1]/4)
for si in range (4):
	for gh in range (13):
		# (left, top, right, bottom)
		caja = (gh*ancho, si*alto, (gh*ancho) + ancho, (si*alto)+alto)
		print(caja)
		region = imagen.crop(caja)
		path = 'cuadrado'+str(si*gh+gh)+'.png'
		print(path)
		region.save(path)


