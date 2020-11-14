import urllib.request
from progress.bar import Bar

def check_net():
    print("Comprobando conexion a internet...")
    try:
        req = urllib.request.Request('http://www.google.com')
        response = urllib.request.urlopen(req)
        print("Conexion a internet activa")

    except urllib.error.URLError:
        print("No dispone de conexion a internet")


bar = Bar('Processing', max=20)
for i in range(20):

    bar.next()
    check_net()
bar.finish()



#loading_bar()
