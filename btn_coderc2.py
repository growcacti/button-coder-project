import tkinter as tk
from tkinter import ttk
from tkinter import font
from tkinter import filedialog, messagebox, Toplevel, Frame, Scrollbar
from tkinter.filedialog import askopenfilename, asksaveasfilename, askdirectory
from tkinter import filedialog

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
        self.frm1 = ttk.Frame(self.parent, width=1200, height=900)
        self.frm1.grid(row=1, column=4)
        self.txt = st.ScrolledText(self.top, height=50, width=100, bg='white',bd=15)
        self.txt.grid(row=2, column=0,sticky="nsew")
        self.btn1 = tk.Button(self.frm1, text="imports", bg="orange", bd=6,command=self.qukimp)
        self.btn1.grid(row=5, column=1)
        self.btn2 = tk.Button(self.frm1, text="Entry", bg="orange",bd =6, command=self.e_code)
        self.btn2.grid(row=6, column=1)
        self.btn3 = tk.Button(self.frm1, text="Button Code1", bg="orange",bd=6, command=self.button_code)
        self.btn3.grid(row=7, column=1)
        self.btn4 = tk.Button(self.frm1, text="Button code2", bg="orange", bd=6,command=self.button_code2)
        self.btn4.grid(row=8, column=1)
        self.btn5 = tk.Button(self.frm1, text="Menu OOP", bg="violet",bd =8, command=self.menu)
        self.btn5.grid(row=9, column=1)
        self.btn6 = tk.Button(self.frm1, text="Label1", bg="orange",bd=8, command=self.label_code1)
        self.btn6.grid(row=10, column=1)
        self.btn7 = tk.Button(self.frm1, text="Label2", bg="orange",bd=6, command=self.label_code2)
        self.btn7.grid(row=11, column=1)
        self.btn8 = tk.Button(self.frm1, text="Notebook empty tabs", bg="orange", bd=6,command=self.notebook)
        self.btn8.grid(row=12, column=1)
        self.btn9 = tk.Button(self.frm1, text="Canvas1", bg="light blue",bd=8, command=self.canvascol)
        self.btn9.grid(row=13, column=1)
        self.btn10 = tk.Button(self.frm1, text="Canva2", bg="orange",bd=8, command=self.canvasrow)
        self.btn10.grid(row=14, column=1)
        self.btn11 = tk.Button(self.frm1, text="combobox", bg="orange", bd=8, command=self.combo_code)
        self.btn11.grid(row=15, column=1)
        self.btn12 = tk.Button(self.frm1, text="combobox2", bg="orange",bd=8, command=self.combo_code2)
        self.btn12.grid(row=16, column=1)
        self.btn13 = tk.Button(self.frm1, text="spin box", bg="orange", bd=6,command=self.spin_code)
        self.btn13.grid(row=17, column=1)
        self.btn14 = tk.Button(self.frm1, text="spinbox2", bg="orange",bd=6, command=self.spin_code2)
        self.btn14.grid(row=18, column=1)
        self.btn15 = tk.Button(self.frm1, text="Text box", bg="light blue",bd=6, command=self.text_code)
        self.btn15.grid(row=19, column=1)
        self.btn16 = tk.Button(self.frm1, text="Slider", bg="orange", bd=6,command=self.slider)
        self.btn16.grid(row=20, column=1)
        self.btn17 = tk.Button(self.frm1, text="Clear", bg="orange",bd=6, command=self.clear)
        self.btn17.grid(row=21, column=1)
        self.btn18 = tk.Button(self.frm1, text="Save", bg="orange",bd=6, command=self.save_code)
        self.btn18.grid(row=22, column=1)
        self.btn19 = tk.Button(self.frm1, text="Open", bg="orange", bd=6, command=self.open_code)
        self.btn19.grid(row=23, column=1)
        self.btn20 = tk.Button(self.frm1, text="self.", bg="orange", bd=6,command=self.insert_self)
        self.btn20.grid(row=0, column=1)
        self.btn21 = tk.Button(self.frm1, text="starter code", bg="orange",bd = 6, command=self.start_code)
        self.btn21.grid(row=0, column=2)
        self.btn23 = tk.Button(self.frm1, text="scrolltext", bg="orange",bd=6, command=self.scrolledtxt)
        self.btn23.grid(row=3, column=2)
        self.btn24 = tk.Button(self.frm1, text="10 chkbuttons", bg="orange", bd=6,command=self.chkbtn10)
        self.btn24.grid(row=4, column=2)
        self.btn25 = tk.Button(self.frm1, text="-------", bg="violet",bd =8, command=self.menu)
        self.btn25.grid(row=5, column=2)
        self.btn26 = tk.Button(self.frm1, text="----", bg="orange",bd=8, command=self.label_code1)
        self.btn26.grid(row=6, column=2)
        self.btn27 = tk.Button(self.frm1, text="-----", bg="orange",bd=6, command=self.label_code2)
        self.btn27.grid(row=7, column=2)
        self.btn28 = tk.Button(self.frm1, text="--------", bg="orange", bd=6,command=self.notebook)
        self.btn28.grid(row=8, column=2)
        self.btn29 = tk.Button(self.frm1, text="----", bg="light blue",bd=8, command=self.canvascol)
        self.btn29.grid(row=9, column=2)
        self.btn30 = tk.Button(self.frm1, text="-------", bg="orange",bd=8, command=self.canvasrow)
        self.btn30.grid(row=10, column=2)
        self.btn31 = tk.Button(self.frm1, text="------", bg="orange", bd=8, command=self.combo_code)
        self.btn31.grid(row=11, column=2)
        self.btn32 = tk.Button(self.frm1, text="-------", bg="orange",bd=8, command=self.combo_code2)
        self.btn32.grid(row=10, column=3)
        self.btn33 = tk.Button(self.frm1, text="--------", bg="orange", bd=6,command=self.spin_code)
        self.btn33.grid(row=11, column=3)
        self.btn34 = tk.Button(self.frm1, text="-------", bg="orange",bd=6, command=self.spin_code2)
        self.btn34.grid(row=12, column=3)
        self.btn35 = tk.Button(self.frm1, text="-----", bg="light blue",bd=6, command=self.text_code)
        self.btn35.grid(row=13, column=3)
        self.btn36 = tk.Button(self.frm1, text="slider", bg="orange", bd=6,command=self.slider)
        self.btn36.grid(row=14, column=3)
        self.btn37 = tk.Button(self.frm1, text="clear", bg="orange",bd=7, command=self.clear)
        self.btn37.grid(row=15, column=3)
        self.btn38 = tk.Button(self.frm1, text="save", bg="orange",bd=7, command=self.save_code)
        self.btn38.grid(row=16, column=3)
        self.btn39 = tk.Button(self.frm1, text="open", bg="orange", bd=6, command=self.open_code)
        self.btn39.grid(row=17, column=3)
       

    def start_code(self):
        starter = ("""
import tkinter
from tkinter import *




class Something(object):
    def __init__(self, *args, *kwargs):
        self.var1 = 0
        self.var2 = 0
        self.var3 = None
        self.var4 = 0
        self.method1()
    def method1(self):
        """)
        self.txt.insert(tk.END, starter)


        
    def insert_self(self):
        self.str = ("""
        self.""")
        self.txt.insert(tk.END, self.str)

    def qukimp(self):
        qpo = (
        """

import tkinter as tk
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
            """
    self.b1 = tk.Button(root,relief=tk.FLAT, compound=tk.LEFT,text="new",command=None)
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





    def label_code1(self):
       
        label_str = (
            """self.label1 = tk.Label(self,
            self.ft = tkFont.Font(family='Ariel Black',size=10)
            self.label1["font"] = ft
            self.label1["fg"] = "#333333",
            self.label1["justify"] = "center",
            self.label1["text"] = "label",
            width=100,height=25)
self.label1.grid(row=4, column=2)"""
            + "\n"
        )
        label_str2 = label_str.replace("self.label1", "self.label" + str(self.labelcount))
        label_str3 = label_str2.replace("row=1", "row=" + str(self.rowcount))
        self.txt.insert(tk.END, label_str3)
        self.labelcount += 1
        self.rowcount += 1

    def label_code2(self):
    
        label_str = (
            """self.label1 = tk.Label(self,
            self.ft = tkFont.Font(family='Ariel Black',size=10)
            self.label1["font"] = ft
            self.label1["fg"] = "#333333",
            self.label1["justify"] = "center",
            self.label1["text"] = "label",
            width=100,height=25)
self.label1.grid(row=5, column=2)"""
            + "\n"
        )
        label_str2 = label_str.replace("self.label1", "self.label" + str(self.labelcount))
        label_str3 = label_str2.replace("column=1", "column=" + str(self.columncount))
        text.insert(tk.END, label_str3)
        self.labelcount += 1
        self.columncount += 1



    def canvascol(self):

        canvas_str = (
                    """
        self.canvas1 = tk.Canvas(self, height=300, width=800, background="cornsilk")
        #self.canvas1.configure( )
        self.canvas1.grid(row=1, column=1)
        #self.canvas1.create_line(x1, y1, x2, y2, fill="black" width=1)"""
                    + "\n"
        )

        canvas_str2 = canvas_str.replace("self.canvas1", "self.canvas" + str(self.canvascount))

        canvas_str3 = canvas_str2.replace("column=1", "column=" + str(self.columncount))
        self.txt.insert("1.0", canvas_str3)
        self.canvascount += 1
        self.columncount += 1

    def canvasrow(self):
      

        canvas_str = (
                """
    self.canvas1 = tk.Canvas(self, height=300, width=800, background="cornsilk")
    self.canvase grid(row=1, column=1)"""
            + "\n"
        )

        canvas_str2 = canvas_str.replace("self.canvas1", "self.canvas" + str(self.canvascount))
        
        canvas_str4 = canvas_str2.replace("row=1", "row=" + str(self.rowcount))
        self.txt.insert("1.0", canvas_str4)
        self.canvascount += 1
        self.rowcount += 1

    def combo_code(self):
    
        combo_str = (
            """
    self.cb1 = ttk.Combobox(self, values=["Value1", "value2, "value3"])
    self.cb1.grid(column=0, row=1)"""
            + "\n"
        )
        combo_str2 = combo_str.replace("self.cb1", "self.cb" + str(self.combocount))
        combo_str3 = combo_str2.replace("row=1", "row=" + str(rowcount))
        self.txt.insert(tk.END, combo_str3)
        self.combocount += 1
        self.rowcount += 1

    def combo_code2(self):
    
        combo_str = (
                """
    self.cb1 = ttk.Combobox(self, values=["Value1", "value2, "value3"])
    self.cb1.grid(column=1, row=1)"""
            + "\n"
        )
        combo_str2 = combo_str.replace("self.cb1", "self.cb" + str(self.combocount))
        combo_str3 = combo_str2.replace("column=1", "column=" + str(self.columncount))
        self.txt.insert(tk.END, combo_str3)
        self.combocount += 1
        self.columncount += 1

    def spin_code(self):
       
        spin_str = (
            """
    self.sp1 = tk.Spinbox(self, from_=1.0, to=1000.0, increment=0.1)
    self.sp1.grid(row=1, column=0)"""
            + "\n"
        )
        spin_str2 = spin_str.replace("self.sp1", "self.sp" + str(self.spincount))
        spin_str3 = spin_str2.replace("row=1", "row=" + str(self.rowcount))
        self.txt.insert(tk.END, spin_str3)
        self.spincount += 1
        self.rowcount += 1

    def spin_code2(self):
      
        spin_str = (
            """
    self.sp1 = tk.Spinbox(self, from_=1.0, to=1000.0, increment=0.1)
    self.sp1.grid(row=1, column=0)"""
            + "\n"
        )
        spin_str2 = spin_str.replace("self.sp1", "self.sp" + str(self.spincount))
        spin_str3 = spin_str2.replace("column=1", "column=" + str(self.columncount))
        self.txt.insert(tk.END, spin_str3)
        self.spincount += 1
        self.columncount += 1

    def text_code(self):
       
        txt_str = (
            """
        self.txt1 = tk.Text(self, height=60, width=150, bg='white')
        self.txt1.insert('1.0', tk.END)
        self.txt1.grid(row=2, column=3)"""
            + "\n"
        )
        txt_str2 = txt_str.replace("txt1", "txt" + str(self.textcount))
        self.txt.insert(tk.END, txt_str2)
        self.textcount += 1

    def slider(self):
        sld_str = ("""
        self.slider1 = ttk.Scale(
            self,
            from_=0,
            to=100,
            orient='vertical',  # horizontal

        """ + "\n")
        slider_str2 = slidar_str.replace("self.slider1", "self.slider" + str(self.slidercount))
        self.txt.insert(tk.END, slider_str2)
        self.slidercount += 1
        self.txt.insert(tk.END, sld_str)

    def chkbtn10(self):
         chkstr =("""
        self.chk1 = IntVar()
        self.chk2 = IntVar()
        self.chk3 = IntVar()
        self.chk4 = IntVar()
        self.chk5 = IntVar()
        self.chk6 = IntVar()
        self.chk7 = IntVar()
        self.chk8 = IntVar()
        self.chk9 = IntVar()
        self.chk10 = IntVar()

        self.chkbtn1 = tk.Checkbutton(
            root, text="   ", variable=self.chk1, onvalue=1, offvalue=0, height=2, width=10
        )

        self.chkbtn2 = Checkbutton(
            root, text="   ", variable=self.chk2, onvalue=1, offvalue=0, height=2, width=10
        )

        self.chkbtn3 = Checkbutton(
            root, text="   ", variable=self.chk3, onvalue=1, offvalue=0, height=2, width=10
        )


        self.chkbtn4 = Checkbutton(
            root, text="   ", variable=self.chk4, onvalue=1, offvalue=0, height=2, width=10
        )
        self.chkbtn5 = Checkbutton(
            root, text="   ", variable=self.chk5, onvalue=1, offvalue=0, height=2, width=10
        )
        self.chkbtn6 = Checkbutton(
            root, text="   ", variable=self.chk6, onvalue=1, offvalue=0, height=2, width=10
        )
        self.chkbtn7 = Checkbutton(
            root, text="   ", variable=self.chk7, onvalue=1, offvalue=0, height=2, width=10
        )
        self.chkbtn8 = Checkbutton(
            root, text="   ", variable=self.chk8, onvalue=1, offvalue=0, height=2, width=10
        )
        self.chkbtn9 = Checkbutton(
            root, text="   ", variable=self.chk9, onvalue=1, offvalue=0, height=2, width=10
        )
        self.chkbtn10 = Checkbutton(
            root, text="   ", variable=self.chk10, onvalue=1, offvalue=0, height=2, width=10
        )


        w = Label(root, text=" Title 1 ", font="50")
        w.grid(row=0, column=0)

        aa = Label(root, text=" Title 2 ", font="50")
        aa.grid(row=0, column=1)

        bb = Label(root, text=" Title 3", font="50")
        bb.grid(row=0, column=2)

        cc = Label(root, text="Title 4 ", font="50")
        cc.grid(row=0, column=3)


        self.chkbtn1.grid(row=1, column=3)
        self.chkbtn2.grid(row=2, column=3)
        self.chkbtn3.grid(row=3, column=3)

        self.chkbtn4.grid(row=4, column=3)
        self.chkbtn5.grid(row=5, column=3)
        self.chkbtn6.grid(row=6, column=3)
        self.chkbtn7.grid(row=7, column=3)
        self.chkbtn8.grid(row=8, column=3)
        self.chkbtn9.grid(row=9, column=3)
        self.chkbtn10.grid(row=10, column=3)""")
         self.txt.insert(tk.END, chkstr)                   

    def scrolledtxt(self):
        txtstr = ("""
import tkinter as tk
from tkinter import scrolledtext as st
from tkinter import *
    class Txt_Widget:(object):
        def __init__(self, parent):
            self.parent = parent
            self.txt = st.ScrolledText(self.top, height=50, width=100, bg='white',bd=15)
            self.txt.grid(row=2, column=0, sticky="nsew") """ )

                  
        self.txt.insert(tk.END, txtstr)


    def notebook(self):
        notestr = ("""

#!/usr/bin/env python3
import tkinter as tk
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox as mb
from tkinter.filedialog import askopenfilename, asksaveasfilename, askdirectory
from tkinter import filedialog
from tkinter import Tk, Frame, Button, BOTH, SUNKEN
from tkinter.colorchooser import askcolor
import os, sys, subprocess

import pyautogui as pag
import pyperclip as pc
import runpy
import glob
import time


from tkinter.scrolledtext import ScrolledText 

##from NB1 import *
##from NB2 import *
##from NB3 import *
##from frwidget import *
##from codestrings import *

class Note(tk.Frame):
    def __init__(self, parent):
        super().__init__()
        self.path = os.getcwd()
        self.parent = parent
        self.notebook = ttk.Notebook(self.parent)
        self.notebook.grid(row=0, column=0)
        self.f1 = ttk.Frame(self.notebook, width=1900, height=1080)
        self.f1.grid(row=0, column=1)
       
        self.notebook.add(self.f1, text="TAB1")
        self.f2 = ttk.Frame(self.notebook)
        self.notebook.add(self.f2, text='2')
                       
                      #################################################################Frame 3################################################################
        self.f3 = ttk.Frame(self.notebook)
        self.notebook.add(self.f3, text='3')
     
        #################################################################################################################################################

        self.f4 = ttk.Frame(self.notebook)
        self.notebook.add(self.f4, text='4')
     

              ########################################################################################
        self.f5 = ttk.Frame(self.notebook)
        self.notebook.add(self.f5, text='5')
       


        ########################################################################################





        f6 = ttk.Frame(self.notebook)
        self.notebook.add(f6, text='6')
      


        ########################################################################################





        f7 = ttk.Frame(self.notebook)
        self.notebook.add(f7, text='7')
        


        ########################################################################################



        f8 = ttk.Frame(self.notebook)
        self.notebook.add(f8, text='8')
        

  


        ########################################################################################
        f9 = ttk.Frame(self.notebook)
        self.notebook.add(f9, text='9')
      
    
            
        ########################################################################################




        f10 = ttk.Frame(self.notebook)
        self.notebook.add(f10, text='10')
    
        ########################################################################################
        f11 = ttk.Frame(self.notebook)
        self.notebook.add(f11, text='11')
        
       


        ########################################################################################


        f12 = ttk.Frame(self.notebook)
        self.notebook.add(f12, text='12')
        
      


        ########################################################################################

        f13 = ttk.Frame(self.notebook)
        self.notebook.add(f13, text='13')
       
        

        f14 = ttk.Frame(self.notebook)
        self.notebook.add(f14, text='14')
        

        f15 = ttk.Frame(self.notebook)
        self.notebook.add(f15, text='15')
       
      

         

        f16 = ttk.Frame(self.notebook)
        self.notebook.add(f16, text='16')
        self.txt16 = ScrolledText(f16, height=1212, width=120)


        f17 = ttk.Frame(self.notebook)
        self.notebook.add(f17, text='17')
      

      


        

        f18 = ttk.Frame(self.notebook)
        self.notebook.add(f18, text='18')
        


        f19 = ttk.Frame(self.notebook)
        self.notebook.add(f19, text='19')
        

      

        f20 = ttk.Frame(self.notebook)
        self.notebook.add(f20, text='20')
       
        
        f21 = ttk.Frame(self.notebook)
        self.notebook.add(f21, text='201')
       

        f22 = ttk.Frame(self.notebook)
        self.notebook.add(f22, text='212')
      

        f23 = ttk.Frame(self.notebook)
        self.notebook.add(f23, text='220')
       
        f24 = ttk.Frame(self.notebook)
        self.notebook.add(f24, text='240')


      
def main():
    parent = tk.Tk()
    app=Note(parent)
    parent.mainloop()


if __name__== '__main__':
    main()

""")
        selk.txt.insert("1.0", notestr)






















    def menu(self):
        menustr = ("""
import tkinter as tk
from tkinter import ttk, Toplevel
from tkinter import messagebox as mb
from tkinter.colorchooser import askcolor
from tkinter.filedialog import askopenfilename, asksaveasfilename
from tkinter import filedialog

from tkinter import Button, Frame, Entry, END

from tkinter.scrolledtext import ScrolledText 

import sys
import os



class MenuBar(tk.Menu):
    def __init__(self, parent):
        tk.Menu.__init__(self, parent)
        self.parent= parent
        self.textwidget = ScrolledText(self.parent, height=50, width=100, bg='white',bd=10)
        self.textwidget.grid(row=10, column=0)
        self.menubar = tk.Menu(self.parent, tearoff=False)
        self.file_menu = tk.Menu(self.menubar)
        self.edit_menu = tk.Menu(self.menubar)
        self.view_menu = tk.Menu(self.menubar)
        self.add_cascade(label="File", menu=self.file_menu)
        self.file_menu.add_command(label="New", underline=1, command=lambda : self.clear())
        self.file_menu.add_command(label="Open", underline=1, command=lambda: self.open_file())
        self.file_menu.add_command(label="Save", underline=1, command=lambda:self.save_file())
        self.file_menu.add_command(label="readlines", underline=1, command=lambda : self.readlines())
        self.file_menu.add_command(label="-----", underline=1, command=self.quit)
        self.file_menu.add_command(label="-------", underline=1, command=self.quit)
        self.file_menu.add_command(label="Exit", underline=1, command=self.quit)
        
        self.add_cascade(label="Edit", menu=self.edit_menu)
        self.edit_menu.add_command(label="Cut", accelerator="Ctrl+X", compound="left", underline=0, command=lambda: self.textwidget.event_generate("<<Cut>>"))
        self.edit_menu.add_command(label="Copy", accelerator="Ctrl+C", compound="left", underline=0,  command=lambda: self.textwidget.event_generate('<<Copy>>'))
        self.edit_menu.add_command(label="Paste", accelerator="Ctrl+V", compound="left", underline=0, command=lambda: self.textwidget.event_generate("<<Paste>>"))
        self.edit_menu.add_command(label="Undo", accelerator="Ctrl+Z", compound="left", underline=0, command=lambda: self.undo())
        self.edit_menu.add_command(label="Redo", accelerator="Ctrl+Y", compound="left", underline=0, command=lambda : self.redo())
        self.edit_menu.add_command(label="Find", accelerator="Ctrl+F", compound="left", underline=0, command=lambda :self.find())
        self.edit_menu.add_command(label="Replace", accelerator="Ctrl+Z", compound="left", underline=0, command=lambda : self.replace())
        self.edit_menu.add_command(label="cleartags", accelerator="Ctrl+Z", compound="left", underline=0, command=lambda : self.cleartags())
        self.add_cascade(label="View", menu=self.view_menu)
        self.view_menu.add_command(label="Backgrounbd Color", compound="left", underline=0,  command=lambda: self.change_bg())
        self.view_menu.add_command(label="Foreground Color",compound="left", underline=0, command=lambda: self.change_fg())
        
    def cleartags(self):
        self.textwidget.tag_config('found', foreground ='black', background = 'white')

    def undo(self):
        try:
            
            self.textwidget.edit_undo()
        except:
            print("No previous action")
    def redo(self):
        try:
            self.textwidget.edit_redo()
        except:
            print("No previous action")




    def copy(self, event=None):
        self.clipboard_clear()
        text = self.textwidget.get("sel.first", "sel.last")
        self.clipboard_append(text)

    def cut(self, event):
        self.copy()
        self.delete("sel.first", "sel.last")

    def paste(self, event):
        text = self.selection_get(selection='CLIPBOARD')
        self.insert('insert', text)



    def quit(self):
        sys.exit(0)


    def clear(self):

        self.textwidget.delete("1.0", tk.END)
    def cleare1(self):
        self.e1.delete(0, END)
   

    def change_bg(self):
       
        (triple, hexstr) = askcolor()
        if hexstr:
            self.textwidget.config(bg=hexstr)


    def change_fg(self):
       
        (triple, hexstr) = askcolor()
        
        if hexstr:
            self.textwidget.config(fg=hexstr)


    def command(self):
        pass


    def open_file(self):
       
        '''Open a file for editing.'''
        filepath = askopenfilename(filetypes=[("Python Scripts", "*.py"),("Text Files", "*.txt"),('All Files', '*.*')])
        if not filepath:
            return
        self.textwidget.delete(1.0, tk.END)
        with open(filepath, 'r') as input_file:
            text = input_file.read()
            self.textwidget.insert(tk.END, text)
       
    def save_file(self):
       
        filepath = asksaveasfilename(
            defaultextension='py',
            filetypes=[('All Files', '*.*')],
        )
        if not filepath:
            return
        with open(filepath, 'w') as output_file:
            text = self.textwidget.get(1.0, tk.END)
            output_file.write(text)

    def readlines(self):
        filepath = askopenfilename(
            filetypes=[("All Files", "*.*")]
        )
        if not filepath:
            return
        self.textwidget.delete("1.0", tk.END)
        with open(filepath, "r") as input_file:
            text = input_file.readlines()
            self.textwidget.insert(tk.END, text)
            return filepath2


    def ggtxt(self, textwidget):
        gettxt = self.tx.get("1.0", tk.END)
        self.textwidget.insert(tk.END, gettxt)

   


       
    def edit2(self, name):
        runpy.run_path(path_name="name")
    def find(self):
        top=Toplevel()
        label1 = tk.Label(top, text = "Find").grid(row=1, column=1) 
        entry1 =tk.Entry(top, width=15, bd=12, bg = "cornsilk")
        entry1.grid(row=2, column=1)
       
        def finder():
            # remove tag 'found' from index 1 to END
            self.textwidget.tag_remove('found', '1.0', END)
            entry = entry1.get()
      
         
            if (entry1):
                idx = '1.0'
                while 1:
                    # searches for desired string from index 1
                    idx = self.textwidget.search(entry, idx, nocase = 1,
                                    stopindex = END)
                     
                    if not idx: break
                     
                    # last index sum of current index and
                    # length of text
                    lastidx = '% s+% dc' % (idx, len(entry))
                     
         
                    # overwrite 'Found' at idx
                    self.textwidget.tag_add('found', idx, lastidx)
                    idx = lastidx
     
            # mark located string as red
             
                self.textwidget.tag_config('found',background="purple", foreground ='yellow')
              
        self.find_btn = tk.Button(top, text="Find", bd=8,command=finder)
        self.find_btn.grid(row=8, column=1)
        entry1.focus_set() 
    

    def replace(self):
        top=Toplevel()
        label1 = tk.Label(top, text = "Find").grid(row=1, column=1) 
        entry1 =tk.Entry(top, width=15, bd=12, bg = "cornsilk")
        entry1.grid(row=2, column=1)
        label2 = tk.Label(top, text = "Replace With ").grid(row=3, column=1)
        entry2 = tk.Entry(top, width=15, bd=12, bg = "seashell")
        entry2.grid(row=5, column=1)
        def replacer():
            # remove tag 'found' from index 1 to END
            self.textwidget.tag_remove('found', '1.0', END)
             
            # returns to widget currently in focus
            self.fin = entry1.get()
            self.repl = entry2.get()
             
            if (self.fin and self.repl):
                idx = '1.0'
                while 1:
                    # searches for desired string from index 1
                    idx = self.textwidget.search(self.fin, idx, nocase = 1,
                                    stopindex = END)
                    print(idx)
                    if not idx: break
                     
                    # last index sum of current index and
                    # length of text
                    lastidx = '% s+% dc' % (idx, len(self.fin))
         
                    self.textwidget.delete(idx, lastidx)
                    self.textwidget.insert(idx, self.repl)
         
                    lastidx = '% s+% dc' % (idx, len(self.repl))
                     
                    # overwrite 'Found' at idx
                    self.textwidget.tag_add('found', idx, lastidx)
                    idx = lastidx
     
            # mark located string as red
            self.textwidget.tag_config('found', foreground ='green', background = 'yellow')
        self.replace_btn = tk.Button(top, text="Find & Replace", bd=8,command=replacer)
        self.replace_btn.grid(row=8, column=1)
        entry1.focus_set()            
class App(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        menubar = MenuBar(self)
        self.config(menu=menubar)

if __name__ == "__main__":
    app=App()
    app.mainloop()


""")
        self.txt.insert("1.0", menustr)



    def clear(self):
        self.txt.delete("1.0", tk.END)

    def open_code(self):
        # file type
        filetypes = [
            ("Python files", "*.py"),
            ("text files", "*.txt"),
            ("All files", "*.*"),
        ]
        # show the open file dialog
        f = filedialog.askopenfile(filetypes=filetypes)
        # read the text file and show its content on the Text
        self.txt.insert("1.0", f.read)




    def save_code(self):
        stop_str = ("""
if __name__== '__main__':
    app = App()
    app.mainloop()""")
        self.txt.insert(tk.END, stop_str)

     
        filepath = asksaveasfilename(
            defaultextension='.py',
            filetypes=[("Python", "*.py"), ("All Files", "*.*")])
        
        if not filepath:
            return
        with open(filepath, 'w') as output_file:
            text = self.txt.get(1.0, tk.END)
            output_file.write(text)

   










class App(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        c = Coder(self)

if __name__ == "__main__":
    app=App()
    app.mainloop()
