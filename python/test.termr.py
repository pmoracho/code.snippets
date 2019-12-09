from tkinter import ttk
from tkinter import Tk
from tkinter import Frame
from tkinter import BOTH, YES
from subprocess import Popen, PIPE
import os
import time

root = Tk()
termf = Frame(root, height=400, width=500)

termf.pack(fill=BOTH, expand=YES)
wid = termf.winfo_id()

with Popen('xterm -into %d -geometry 10x40 -sb ' % wid, shell=True,
					stdin=PIPE, bufsize=1, universal_newlines=True) as proc:
	pass

root.mainloop()

