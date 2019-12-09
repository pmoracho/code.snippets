import tkinter as tk, threading
import imageio
from PIL import Image, ImageTk
from tkinter import *
from tkinter import Tk    
from tkinter import PhotoImage
from tkinter import Canvas
from tkinter import NW
from tkinter import Menu
from tkinter import filedialog
from PIL import Image, ImageTk
from sys import argv
import tkinter as tk
from tkinter.filedialog import askopenfilename
import cv2
import os
from keras.models import model_from_json
from keras.optimizers import SGD
import numpy as np
from time import sleep

ventana = tk.Tk()
#ventana.bind('<escape>', lambda e: root.quit())
#define CV_HAAR_FEATURE_MAX   3
#ventana.geometry("1800x900")
#tamaño maximizada de la ventana
m = ventana.maxsize()
ventana.geometry('{}x{}+0+0'.format(*m))
#ventana.geometry("900x900+0+0")
ventana.configure(background="black")
#-------------------------------------
ventana.title("Sistema para el análisis de actitud")
#fondo=PhotoImage(file="popo.gif")
#lblFondo=Label(ventana,image=fondo).place(x=0,y=0) #fondo 


"""

img_frame = tk.Frame(ventana, height=600, width=800, bg='#faf0e6')
img_frame.pack()
canvas = tk.Canvas (img_frame, height=600, width=800, bg='#faf0e6', relief=tk.SUNKEN)

sbarV = tk.Scrollbar(img_frame, orient=tk.VERTICAL, command=canvas.yview)
sbarH = tk.Scrollbar(img_frame, orient=tk.HORIZONTAL, command=canvas.xview)
sbarV.pack(side=tk.RIGHT, fill=tk.Y)
sbarH.pack(side=tk.BOTTOM, fill=tk.X)

canvas.config(yscrollcommand=sbarV.set)
canvas.place(x=50, y=0)
canvas.config(xscrollcommand=sbarH.set)
canvas.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)"""

# Variable global que va a contener el video


##--------FONDO DE PANTALLA PARA LA INTERFAZ----------------------
image= Image.open("fondo1.gif")
img_copy = image.copy()
background_image = ImageTk.PhotoImage(image)
background = Label(ventana,image=background_image)
background.place(x=0, y=0)
background.pack(fill=BOTH, expand=YES)

new_width = 1600
new_height = 800
image = img_copy.resize((new_width, new_height))
background_image = ImageTk.PhotoImage(image)
background.configure(image = background_image)

background.pack(fill=BOTH, expand=YES)
#-----------------------------------------------------------------------

"""video_name = "pruebaMay.mp4" #This is your video file path
video = imageio.get_reader(video_name)"""

model = model_from_json(open('./models/my_cnn_tflearn.json').read())#modelo de clasificaci-on creado por la red neuronal
#model.load_weights('_model_weights.h5')
model.load_weights('./models/my_cnn_tflearn.h5')#aqui se carga el ventor
sgd = SGD(lr=0.1, decay=1e-6, momentum=0.9, nesterov=True)
model.compile(loss='categorical_crossentropy', optimizer=sgd)

ruta = None
conAle = None 
#-------- Aquí se abre el cuadro de dialogo para abrir el video --------------------
def abrir():
    global ruta
    ventana.filename=filedialog.askopenfilename(initialdir="/Users/niet/Desktop")
    ruta=ventana.filename
#-------------------------------------------------------------------------------------


#--------- Aqui se hace el reconocimiento de expresiones faciales
import matplotlib.pyplot as plt
def detectar():
    global ruta
    global conAle
    global conEno
    global conMie
    global conDis
    global conSor
    global conTri
    #ventana.filename=filedialog.askopenfilename(initialdir="/Users/niet/Desktop")
    #ruta=ventana.filename
    video_capture =  cv2.VideoCapture(ruta)#desde video creado
    def extract_face_features(gray, detected_face, offset_coefficients):
        (x, y, w, h) = detected_face
        #print x , y, w ,h
        horizontal_offset = np.int(np.floor(offset_coefficients[0] * w))
        vertical_offset = np.int(np.floor(offset_coefficients[1] * h))
    

        extracted_face = gray[y+vertical_offset:y+h, 
                          x+horizontal_offset:x-horizontal_offset+w]
        #print extracted_face.shape
        new_extracted_face = zoom(extracted_face, (48. / extracted_face.shape[0], 
                                               48. / extracted_face.shape[1]))
        new_extracted_face = new_extracted_face.astype(np.float32)
        new_extracted_face /= float(new_extracted_face.max())
        return new_extracted_face
    from scipy.ndimage import zoom
    def detect_face(frame):
            cascPath = "./models/haarcascade_frontalface_default.xml"#algoritmo para la detección de rostro
            faceCascade = cv2.CascadeClassifier(cascPath)
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            detected_faces = faceCascade.detectMultiScale(
                    gray,
                    scaleFactor=1.1,
                    minNeighbors=6,
                    minSize=(48, 48),
                    #flags=cv2.CV_HAAR_FEATURE_MAX)
                    flags=2)
            return gray, detected_faces

    cascPath = "haarcascade_frontalface_default.xml"
    faceCascade = cv2.CascadeClassifier(cascPath)

    #video_capture = cv2.VideoCapture(0)#tiempo real
    Tk().withdraw()
    #Cuadro de dialogo para abrir desde escritorio
    #print(filename)#imprime la dirección del archivo
    #video_capture =  cv2.VideoCapture(ruta,0)#desde video creado
    conAle = 0
    conEno = 0
    conDes = 0
    conMie = 0
    conTri = 0
    conSor = 0
    while (True):
        #el video se captura frame por frame
        sleep(0.0)
        ret, frame = video_capture.read()

        #detecta el rostro
        gray, detected_faces = detect_face(frame)
        
        face_index = 0
        contador = 0
       
        
        # etiquetado de las expresiones faciales
        for face in detected_faces:
            (x, y, w, h) = face
            if w > 100:
                cv2.rectangle(frame, (x, y), (x+w, y+h), (75, 0, 130), 2)#el rectangulo de la cara
                
                extracted_face = extract_face_features(gray, face, (0.075, 0.05)) #(0.075, 0.05) extracción  de caracteristicas
                prediction_result = model.predict_classes(extracted_face.reshape(1,48,48,1))


                # Etiquetado de la expresión
                if prediction_result == 3:
                    cv2.putText(frame, "Alegria",(x,y), cv2.FONT_ITALIC, 2, (255, 215, 0), 2)
                    conAle = conAle + 1
                    
                elif prediction_result == 0:
                    cv2.putText(frame, "Enojo",(x,y), cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 215, 0), 2)
                    conEno = conEno + 1

                elif prediction_result == 1:
                    cv2.putText(frame, "Disgusto",(x,y), cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 215, 0), 2)
                    conDis = conDis + 1

                elif prediction_result == 2:
                    cv2.putText(frame, "Miedo",(x,y), cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 215, 0), 2)
                    conMie = conMie + 1

                elif prediction_result == 4:
                    cv2.putText(frame, "Tristeza",(x,y), cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 215, 0), 2)
                    conTri = conTri + 1
                else :
                    cv2.putText(frame, "Sorpresa",(x,y), cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 215, 0), 2)
                    conSor = conSor + 1
               
                #print("Expresiones de alegría son: ", conAle) 
                # increment counter
                face_index += 1
                contador = face_index+contador
        print("Expresiones de alegría son: ", conAle) 

            
    

         

        # Muestra el reconocimiento de expresiones faciales
        cv2.imshow('Video', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            #break
            break   
    fig = plt.figure()
    ax = fig.add_subplot(111)

    graficar = [10,8,9,10,7]
    xx = range(len(graficar))
    ax.bar(xx,graficar)
    plt.show()
    #Cuando todo esta hecho libera la captura
    video_capture.release()
    cv2.destroyAllWindows()

    

    
# -------------Información de las funciones del sistema --------------------------------
class Acerca:
    def __init__(self, parent):
        text = ("      Acerca del sistema\n\n        "
                "***** Opción de archivo *****\n"
                "Archivo:En este menú se encuentran los submenús: Abri y Salir \n"
                "Abrir: Muestra un cuadro de dialógo donde podra seleccionar el video que usted decida\n"
                "Salir: Con esta opción podra salir del sistema "
                "***** Opción de Reconocimiento *****\n"
                "Reconocimiento:En este menú muestra la opción para el reconocimiento de expresiones faciales \n"
                "Detección: Esta opción permite la detección de las seis expresiones faciales en la secuencia del video \n"
                )

        self.top = tk.Toplevel(parent)
        self.top.title("Acerca de ")
        display = tk.Text(self.top)
        display.pack()
        display.insert(tk.INSERT, text)
        display.config(state=tk.DISABLED)
        b = tk.Button(self.top, text="Cerrar", command=self.cerrar)
        b.pack(pady=5)
        b.config(bg="CadetBlue")## bg es el boton de cerrar ,aqui se puede cambiar

    def cerrar(self):
        self.top.destroy()

class Main_Window:
    def __init__(self,  ventana):
        mnuAcerca.add_command(label="Acerca de ",command=self.ayuda)
    def ayuda(self):
        Acerca(ventana)
#----------------------------------------------------------------------------------------------


#---------------Ayuda para ánalizar un video -------------------------
class Ayuda:
    def __init__(self, parent):
        text = ("      Ánalisis  de un video \n"
                "[1] Seleccionar el video con la opción Abrir\n"
                "[2] Seleccionar la opción detección, para el reconocimiento de expresiones faciales \n"
                "[3] Imprimir reportes\n"
                )
        self.top = tk.Toplevel(parent)
        self.top.title("Ayuda")
        display = tk.Text(self.top)
        display.pack()
        display.insert(tk.INSERT, text)
        display.config(state=tk.DISABLED)
        b = tk.Button(self.top, text="Cerrar", command=self.cerrar)
        b.pack(pady=5)
        b.config(bg="CadetBlue")## bg es el boton de cerrar ,aqui se puede cambiar

    def cerrar(self):
        self.top.destroy()

class Main_Window1:
    def __init__(self,  ventana):
        mnuAcerca.add_command(label="Sistema de reconocimiento 'AYUDA' ",command=self.ayuda)
    def ayuda(self):
        Ayuda(ventana)
#-----------------------------------------------------------------------------------------

def imprimirG():
    global conAle
    global conEno
    global conMie
    global conDis
    global conSor
    global conTri
    fig = plt.figure()
    ax = fig.add_subplot(111)

    datos = [10,8,9,10,7]
    xx = range(len(datos))
    ax.bar(xx,datos)
    plt.show()


barraMenu=Menu(ventana)
#crear los menús .............................................................. 
mnuArchivo=Menu(barraMenu)
mnuDiagnostico=Menu(barraMenu)
mnuReporte=Menu(barraMenu)
mnuAyuda=Menu(barraMenu)
mnuAcerca=Menu(barraMenu)
#crear los comandos de los menús................................................
mnuArchivo.add_command(label="Abrir", command = abrir)
mnuArchivo.add_separator()
mnuArchivo.add_command(label="Salir")

mnuDiagnostico.add_command(label="Detección ", command = detectar)

mnuReporte.add_command(label="Imprimir", command = imprimirG)

######################...........................................................
barraMenu.add_cascade(label="Archivo",menu=mnuArchivo)
barraMenu.add_cascade(label="Reconocimiento",menu=mnuDiagnostico)
barraMenu.add_cascade(label="Reportes",menu=mnuReporte)
barraMenu.add_cascade(label="Ayuda ",menu=mnuAcerca)
ventana.config(menu=barraMenu)



if __name__ == "__main__":
    Main_Window(ventana)
    Main_Window1(ventana)

ventana.mainloop()
