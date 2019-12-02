'''
PROYECTO LENGUAJES DE PROGRAMACIÓN
INTEGRANTES: JOEL ESPINOZA - CHRISTIAN GUERRERO - FABRICIO HERRERA
PARALELO 1
'''

import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QGridLayout
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QTextEdit
from PyQt5.QtWidgets import QTextBrowser
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QLabel
from PyQt5.QtCore import Qt
import tkinter as tk
from tkinter import scrolledtext as st
import sys
from tkinter import filedialog as fd
from tkinter import messagebox as mb
from ProductosCorrectos_Lexer import *
from ProductosCorrectos_Parser import *

class window:
    def __init__(self):
        self.contenedor=tk.Tk()
        self.contenedor.title("Analizador")
        self.contenedor.geometry("1350x500")

        self.crearLabel()
        self.crearMain()
        self.textAreaCodigo=st.ScrolledText(self.contenedor, width=60, height=20)
        self.textAreaCodigo.grid(column=0,row=2, padx=10, pady=10)
        self.textAreaAnalizar= st.ScrolledText(self.contenedor, width=60, height=20)
        self.textAreaAnalizar.grid(column=3,row=2, padx=10, pady=10)
        self.crearButton()
        self.textAreaResult= st.ScrolledText(self.contenedor, width=30, height=5)
        self.textAreaResult.grid(column=2, row=2, padx=20, pady=10)
        self.contenedor.mainloop()

    def crearLabel(self):
        Label1 = tk.Label(self.contenedor,text="Codigo:")
        Label1.grid(column=0, row=1)
        Label1.pack
        Label2 = tk.Label(self.contenedor,text="Analizador:")
        Label2.grid(column=3, row=1)
        Label2.pack



    def crearMain(self):
        menuTop = tk.Menu(self.contenedor)
        self.contenedor.config(menu=menuTop)
        opciones = tk.Menu(menuTop, tearoff=0)
        menuTop.add_cascade(label="Opciones de Archivos", menu=opciones)
        opciones.add_separator()
        opciones.add_command(label="Guardar archivo", command=self.guardar_archibo)
        opciones.add_separator()
        opciones.add_command(label="Abrir archivo", command=self.abrir_archivo)
        opciones.add_separator()
        opciones.add_command(label="Salir", command=self.salir)

    def crearButton(self):
        btnLexer = tk.Button(self. contenedor, text="Léxico", command=self.analizar_lexer, width=60)
        btnLexer.grid(column=0, row=3)
        btnLexer.pack
        btnSintactico = tk.Button(self.contenedor, text="Semántico", command=self.analizar_sintactico, width=60)
        btnSintactico.grid(column=0, row=4)
        btnSintactico.pack

    def analizar_sintactico(self):
        tokens = analisis_sem(self.textAreaCodigo.get("1.0", tk.END))
        errors = error_Parser(self.textAreaCodigo.get("1.0", tk.END))
        self.textAreaAnalizar.delete("1.0", tk.END)
        self.textAreaResult.delete('1.0', tk.END)
        for token in tokens:
            self.textAreaAnalizar.insert("1.0", str(token) + "\n")
        if errors == True:
            self.textAreaResult.insert("1.0", "" + "Su codigo no paso la etapa sintáctica\n")
        else:
            self.textAreaResult.insert("1.0", "" + "Su codigo aprobo la etapa sintáctica\n")

    def analizar_lexer(self):
        tokens = analisis_lex(self.textAreaCodigo.get("1.0", tk.END))
        errors = error_lex(self.textAreaCodigo.get("1.0", tk.END))
        self.textAreaResult.delete("1.0", tk.END)
        self.textAreaResult.delete("1.0", tk.END)
        for token in tokens:
            self.textAreaAnalizar.insert("1.0", str(token)+"\n")
        if errors == True:
            self.textAreaResult.insert("1.0", ""+"Su codigo no paso la etapa léxica\n")
        else:
            self.textAreaResult.insert("1.0", ""+"Su codigo aprobo la etapa léxica\n")


    def salir(self):
        sys.exit()

    def guardar_archibo(self):
        nombrearch=fd.asksaveasfilename(initialdir = "/",title = "Guardar como",filetypes = (("txt files","*.txt"),("todos los archivos","*.*")))
        if nombrearch!='':
            archi1=open(nombrearch, "w", encoding="utf-8")
            archi1.write(self.textAreaCodigo.get("1.0", tk.END))
            archi1.close()
            mb.showinfo("Información", "Los datos fueron guardados en el archivo.")


    def abrir_archivo(self):
        nombrearch=fd.askopenfilename(initialdir = "/",title = "Seleccione archivo",filetypes = (("txt files","*.txt"),("todos los archivos","*.*")))
        if nombrearch!='':
            archi1=open(nombrearch, "r", encoding="utf-8")
            contenido=archi1.read()
            archi1.close()
            self.textAreaCodigo.delete("1.0", tk.END)
            self.textAreaCodigo.insert("1.0", contenido)


Ventana=window()