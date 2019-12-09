import pandas as pd
from pandas import ExcelWriter

with pd.ExcelWriter('exportado.xlsx') as writer:
	for i in range(1, 20+1, 1):
		filename = '{0}.csv'.format(i)
		try:
			datos=pd.read_csv(filename)
			df=datos.iloc[:,[2,3,5,6,7,8,9,10,11,12]]
			df.to_excel(writer, startrow=0, header=True, index=False, sheet_name="Ok{0}".format(i), encoding='utf-8')
		except FileNotFoundError:
			print("El archivo {0} no existe".format(filename))

writer.save()
