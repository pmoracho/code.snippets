import sqlite3

con = sqlite3.connect(":memory:")
con.text_factory = str
cur = con.cursor()

fila = (1, 'Cadena')

cur.execute("create table prueba(id int, cadena TEXT)")
cur.execute("insert into prueba(id, cadena) values(?, ?)", fila)
cur.execute("select * from prueba")
for row in cur.fetchall():
    print("Cadena:", row[1])


con.close()


x = u'Cadena'
lista = [x]
print(lista)

print(lista[0])