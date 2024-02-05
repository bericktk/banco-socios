# Criando a parte gráfica do projeto
# importações
from tkinter import*
from tkinter import Tk, StringVar, ttk
from PIL import Image, ImageTk

# Palheta de Cores
co0 = "#2e2d2b" # Preto
co1 = "#feffff" # Branco
co2 = "#4fa882" # Verde
co3 = "#38576b" # Valor
co4 = "#403d3d" # Letra
co5 = "#e06636" # - profit
co6 = "#038cfc" # azul
co7 = "#3fbfb9" # Verde
co8 = "#263238" # + verde
co9 = "#e9edf5" # +verde

# Criando janela
janela = Tk()
janela.title('')
janela.geometry('900x600')
janela.configure(background=co9)
janela.resizable(width=FALSE, height=FALSE)

style = ttk.Style(janela)
style.theme_use("clam")

# Criando os frames
# Frame titulo
frametitulo = Frame(janela, width=1043, height=50, bg=co1, relief=FLAT)
frametitulo.grid(row=0, column=0)

# Frame formulário
frameform = Frame(janela, width=1043, height=303, bg=co1, pady=20, relief=FLAT)
frameform.grid(row=1, column=0, pady=1, padx=0, sticky=NSEW)

# Frame final
framebaixo = Frame(janela, width=1043, height=303, bg=co1, pady=20, relief=FLAT)
framebaixo.grid(row=2, column=0, pady=0, padx=0, sticky=NSEW)

# Abrindo imagem
app_img = Image.open('socio.png')
app_img = app_img.resize((45,45))
app_img = ImageTk.PhotoImage(app_img)

app_logo = Label(frametitulo, image=app_img, text=' Banco de Dados CBPCE', width=900, compound=LEFT, relief=RAISED, anchor=NW, font=('Verdana 20 bold'), bg=co1, fg=co4)
app_logo.place(x=0, y=0)

janela.mainloop()
