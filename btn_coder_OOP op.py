import tkinter as tk
from tkinter import ttk
from tkinter import font
from tkinter import filedialog, messagebox, Toplevel, Frame, Scrollbar

# import tkinter.scrolledtext
from tkinter import scrolledtext as st
from tkinter import *
import tkinter.colorchooser
import os, pathlib
import pyautogui as pg
import pyperclip as pc
import glob
import time





class Coder(object):
    ecount = 1
    btncount = 1
    btncount2 = 1
    labelcount = 1
    canvascount = 1
    lboxcount = 1
    rowcount = 1
    columncount = 1
    combocount = 1
    spincount = 1
    textcount = 1
    slidercount = 1
    scrollcount = 1
    projectcount = 1
    def __init__(self,parent):
        self.parent = parent
        self.top = Toplevel()
        self.frm1 = ttk.Frame(self.parent, width=800, height=150)
        self.frm1.grid(row=1, column=1)
        self.txt = st.ScrolledText(self.top, height=50, width=100, bg='white',bd=15)
        self.txt.grid(row=10, column=0,sticky="nsew")
        self.btn1 = tk.Button(self.frm1, text="imports", bg="orange", bd=5,command=self.qukimp)
        self.btn1.grid(row=5, column=1)
        self.btn2 = tk.Button(self.frm1, text="Entry", bg="orange",bd =5, command=self.e_code)
        self.btn2.grid(row=6, column=1)
        self.btn3 = tk.Button(self.frm1, text="Button Code1", bg="orange", command=self.button_code)
        self.btn3.grid(row=7, column=1)
        self.btn4 = tk.Button(self.frm1, text="Button code2", bg="orange", command=self.button_code2)
        self.btn4.grid(row=8, column=1)
##        self.btn5 = tk.Button(self.frm1, text="ctlr alt t", bg="violet", command=pg4)
##        self.btn5.grid(row=9, column=1)
##        self.btn6 = tk.Button(self.frm1, text="terminal", bg="orange", command=pg5)
##        self.btn6.grid(row=10, column=1)
##        self.btn7 = tk.Button(self.frm1, text="open app", bg="orange", command=pg6)
##        self.btn7.grid(row=11, column=1)
##        self.btn8 = tk.Button(self.frm1, text="alt F4 close", bg="orange", command=pg7)
##        self.btn8.grid(row=12, column=1)
##        self.btn9 = tk.Button(self.frm1, text="pg.moveTo", bg="light blue", command=pg8)
##        self.btn9.grid(row=13, column=1)
##        self.btn10 = tk.Button(self.frm1, text="apt udate", bg="orange", command=pg9)
##        self.btn10.grid(row=14, column=1)
##        self.btn11 = tk.Button(self.frm1, text="self.btn1", bg="orange", command=pg10)
##        self.btn11.grid(row=15, column=1)
##        self.btn12 = tk.Button(self.frm1, text="self.btn1", bg="orange", command=pg11)
##        self.btn12.grid(row=16, column=1)
##        self.btn13 = tk.Button(self.frm1, text="self.btn1", bg="orange", command=pg12)
##        self.btn13.grid(row=17, column=1)
##
##





    def qukimp(self):
        qpo = (
        """import tkinter as tk
from tkinter import ttk
from tkinter import font
from tkinter import filedialog, messagebox, Toplevel, Frame
from tkinter import *
import os, pathlib
import pyautogui as pg
import pyperclip as pc
import glob
import time"""
            + "\n"
        )
        self.txt.insert(tk.END, qpo)


    def e_code(self):
      
        w_str = (
            """    self.var = tk.StringVar(self)
    self.e1 = tk.Entry(self, self.textvariable=self.var, bg='snow')
    self.e1.grid(row=3, column=4)"""
            + "\n"
        )
        w_str2 = w_str.replace("self.var1", "self.var" + str(self.ecount))
        w_str3 = w_str2.replace("self.e1", "self.e" + str(self.ecount))
        w_str4 = w_str3.replace("row=3", "row=" + str(self.rowcount))
        self.txt.insert(tk.END, w_str4)
        self.ecount += 1
        self.rowcount += 1

    def button_code(self):
       
        w_str = (
            """    self.b1 = tk.Button(root,relief=tk.FLAT, compound=tk.LEFT,text="new",command=None)
    self.b1.grid(row=1, column=2)"""
            + "\n"
        )
        w_str2 = w_str.replace("b1", "b" + str(self.btncount))
        w_str3 = w_str2.replace("row=1", "row=" + str(self.rowcount))
        self.txt.insert(tk.END, w_str3)
        self.btncount += 1
        self.rowcount += 1

    def button_code2(self):
    
        w_str = (
            """    self.btn1 = tk.Button(self,
                    relief=tk.FLAT,
                    compound=tk.LEFT,
                    self.text="new",
                    command=None,

                )
self.btn1.grid(row=2, column=1)"""
            + "\n"
        )
        w_str2 = w_str.replace("self.btn1", "self.btn" + str(self.btncount2))
        w_str3 = w_str2.replace("column=1", "column=" + str(self.columncount))
        self.txt.insert(tk.END, w_str3)
        self.btncount2 += 1
        self.columncount += 1

















class App(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        c = Coder(self)

if __name__ == "__main__":
    app=App()
    app.mainloop()
