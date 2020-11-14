from tkinter import *
from tkinter import messagebox
import tkinter as tk
import math

def Basilea():
    a = 0
    b = 0
    for i in range(1, Basilea_limit.get() + 1):
        a = (1 / i ** 2)
        b = a + b
    c = math.sqrt(6*b)
    messagebox.showinfo("Resultado", "El resultado es: " + str(c))


window = tk.Tk()
Basilea_limit = IntVar()
window.geometry("400x100")
window.title("Calculadora de pi")
Message_1 = Label(window, text="Ingresa el limite de Basilea").place(x=0, y=10)
Entrance_1 = Entry(window, textvariable=Basilea_limit).place(x=200, y=10)
Button_1 = Button(window, text="Aceptar", command=Basilea).place(x=150, y=50)
window.mainloop()

SQL = "SELECT * FROM Tabla"
