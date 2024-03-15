import customtkinter as ctk


# Cria a nossa janela
janela = ctk.CTk()

# Configurando a janela principal
janela.title('App Teste')
janela.geometry('700x400')
janela.maxsize(width = 900, height = 550)
janela.minsize(width = 500, height = 300)
janela.resizable(width = False, height = False)


# Configurando o tema
janela._set_appearance_mode('dark')
#janela._set_apperance_mode('dark')
#janela._set_apperance_mode('system')


janela.mainloop()
