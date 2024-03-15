import tkinter as tk
from centralizar_tela import menu_inicial

def abrir_janela():
	janela2 = menu_inicial.mainloop()


janela = tk.Tk()

botao = tk.Button(janela, text = 'Ir para nova janela', command = menu_inicial)
botao.grid(row = 0, column = 0)

janela.mainloop()