import tkinter as tk

janela = tk.Tk()
janela.title("Minha primeira janela")

label = tk.Label(janela, text="Olá, mundo !")
label.pack()
janela.mainloop()