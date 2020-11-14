from tkinter import ttk
import ttk
import tkFileDialog as chooser
from PIL import Image, ImageTk

class VentanaPpal(tk.Tk):

    def __init__(self):
        tk.Tk.__init__(self)
        self.title("Visor de imagenes")
        self.geometry("900x600")
        self.marco = FrameCanvas(maestro=self)
        self.barraMenu = self.crearMenu()
        self.config(menu=self.barraMenu)
        self.imagen = Imagen()
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)

    def crearMenu(self):
        menu = tk.Menu(self)
        menuArchivo = tk.Menu(menu)
        menuArchivo.add_command(label='Abrir Imagen',command=self.marco.cargarImagen)
        menuArchivo.add_separator()
        menuArchivo.add_command(label='Salir', command=self.destroy)
        menu.add_cascade(label='Archivo', menu=menuArchivo)

        return menu

class FrameCanvas(tk.Frame):

    def __init__(self, maestro):
        tk.Frame.__init__(self, master=maestro)
        self.imagen = Imagen()

        #Creacion de las barras de desplazamiento horizontal y vertical
        vbar = tk.Scrollbar(self.master, orient='vertical')
        hbar = tk.Scrollbar(self.master, orient='horizontal')
        vbar.grid(row=0, column=1, sticky='ns')
        hbar.grid(row=1, column=0, sticky='we')

        #Creacion del canvas, area donde se va a mostrar la imagen
        self.canvas = tk.Canvas(self.master, bg='blue', highlightthickness=0, xscrollcommand=hbar.set, yscrollcommand=vbar.set)
        self.canvas.grid(row=0, column=0, sticky='NESW')
        vbar.configure(command=self.canvas.yview)
        hbar.configure(command=self.canvas.xview)
        self.canvas.configure(scrollregion=self.canvas.bbox('all'))

    def cargarImagen(self):
        self.imagen.abrirImagen()
        self.mostrarImagen()

    def mostrarImagen(self):
        img = self.imagen.getImagen()
        if img!= None:
            self.canvas.create_image(0, 0, image=img, anchor='nw')


class Imagen:

    def abrirImagen(self):
        ruta = chooser.askopenfile(title='Seleccionar Imagen')
        if ruta != None:
           self.imagen = ImageTk.PhotoImage(Image.open(ruta))
        else:
           self.imagen = None
