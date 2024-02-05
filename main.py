# Criando a parte gráfica do projeto
# importações
from tkinter import*
from tkinter import Tk, StringVar, ttk

# Palheta de Cores
co0 = "#2e2d2b" # Preto
co1 = "#feffff" # Branco
co2 = "#4fa882" # Verde
co3 = "#38576b" # Valor
co4 = "#403d3d" # Letra


# Criando janela
janela = Tk()
janela.title('')
janela.geometry('900x600')
janela.configure(background=co1)
janela.resizable(width=FALSE, height=FALSE)

janela.mainloop()