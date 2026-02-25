import tkinter as tk
def somar():
    a = int(entrada1.get())
    b = int(entrada2.get())

    resultado = a + b

    l_resultado.config(text=f"Resultado:{resultado}")

def subtrair():
    a = int(entrada1.get())
    b = int(entrada2.get())

    resultado = a - b

    l_resultado.config(text=f"Resultado: {resultado}")
janela = tk.Tk()
janela.title("Calculadora Simples")

entrada1 = tk.Entry(janela)
entrada1.pack()

entrada2 = tk.Entry(janela)
entrada2.pack()

botao = tk.Button(janela, text="Somar", command=somar)
botao.pack()

botao_subtrair = tk.Button(janela, text="Subtrair", command=subtrair)
botao_subtrair.pack()

l_resultado = tk.Label(janela, text="Resultado:")
l_resultado.pack()

janela.mainloop()