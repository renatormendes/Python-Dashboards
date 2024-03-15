from tkinter import *
import tkinter as tk
import funcoes as fc

def abrir_janela():
	fc.consume(mainScreen)


mainScreen = tk.Tk()

mainScreen.geometry('600x420')
mainScreen.title('System')
mainScreen['bg'] = 'cyan'

chama = tk.Button(mainScreen, text = 'Chama o novo form', command = abrir_janela)
chama.place(x = 220, y = 200)

#abrir_janela()
mainScreen.mainloop()

