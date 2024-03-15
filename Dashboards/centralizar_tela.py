'''

Aqui esta uma forma de centralizar uma janela com Python
no Tkinter. Altere somente a largura e a altura para que
o sistema centralize a janela.

'''

from tkinter import *

menu_inicial = tk.Toplevel()
menu_inicial.title("Titulo")


# Dimensões da janela
largura = 800
altura = 600

# Resolução do nosso sistema
lagura_screen = menu_inicial.winfo_screenwidth()
altura_screen = menu_inicial.winfo_screenheight()

print('largura: ', lagura_screen, 'altura: ', altura_screen)

# Posição da janela
posx = lagura_screen/2 - largura/2
posy = altura_screen/2 - altura/2

# Definir a geometria da janela (geometry)
menu_inicial.geometry("%dx%d+%d+%d" % (largura, altura, posx, posy))


menu_inicial.mainloop()