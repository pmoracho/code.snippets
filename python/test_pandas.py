import pandas as pd
from io import StringIO

test_data=StringIO("""asesor;tienda;puntos
A1;t1;1
A1;t2;0
A1;t2;1
A1;t3;1
A1;t3;1
A2;t1;0
A2;t2;1
A3;t4;1
A3;t4;1""")

df = pd.read_csv(test_data, sep=";")

g = df.groupby(['asesor', 'tienda'])['puntos'].sum()
print(g)

print(g.reset_index())


