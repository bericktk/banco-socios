# Criando a parte gráfica do projeto
# importações
from tkinter import*
from tkinter import Tk, StringVar, ttk
from PIL import Image, ImageTk
from tkcalendar import Calendar, DateEntry
from datetime import date

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

# Cabeçário - Frame parte de cima
# Abrindo imagem
app_img = Image.open('socio.png')
app_img = app_img.resize((45,45))
app_img = ImageTk.PhotoImage(app_img)

app_logo = Label(frametitulo, image=app_img, text=' Banco de Dados', width=900, compound=LEFT, relief=RAISED, anchor=NW, font=('Verdana 20 bold'), bg=co1, fg=co4)
app_logo.place(x=0, y=0)

# Formulário(Frame Meio)

# Criando entradas
l_nome = Label(frameform, text="Nome", height=1, anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
l_nome.place(x=10, y=10)
e_nome = Entry(frameform, width=30, justify='left', relief=SOLID)
e_nome.place(x=130, y=11)

l_empresa = Label(frameform, text="Empresa", height=1, anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
l_empresa.place(x=10, y=40)
e_empresa = Entry(frameform, width=30, justify='left', relief=SOLID)
e_empresa.place(x=130, y=41)

l_descricao = Label(frameform, text="Descrição", height=1, anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
l_descricao.place(x=10, y=70)
e_descricao = Entry(frameform, width=30, justify='left', relief=SOLID)
e_descricao.place(x=130, y=71)

l_marca = Label(frameform, text="Marca", height=1, anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
l_marca.place(x=10, y=100)
e_marca = Entry(frameform, width=30, justify='left', relief=SOLID)
e_marca.place(x=130, y=101)

l_cal = Label(frameform, text="Data de Associação", height=1, anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
l_cal.place(x=10, y=130)
e_cal = DateEntry(frameform, width=12, background='darkblue', bordewidth=2, year=2024)
e_cal.place(x=130, y=131)

l_valor_mensalidade = Label(frameform, text="Mensalidade", height=1, anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
l_valor_mensalidade.place(x=10, y=160)
e_valor_mensalidade = Entry(frameform, width=30, justify='left', relief=SOLID)
e_valor_mensalidade.place(x=130, y=161)

l_serie = Label(frameform, text="Número de Série", height=1, anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
l_serie.place(x=10, y=190)
e_serie = Entry(frameform, width=30, justify='left', relief=SOLID)
e_serie.place(x=130, y=191)

# Criando os botões
# Botão Carregar Logo
l_carregar_imagem = Label(frameform, text="Logo da Empresa", height=1, anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
l_carregar_imagem.place(x=10, y=220)
b_carregar_imagem = Button(frameform, width=30, text="Carregar", compound=CENTER, anchor=CENTER, overrelief=RIDGE, font=('Ivy 8'), bg=co1, fg=co0)
b_carregar_imagem.place(x=130, y=221)

# Botão Adicionar ou Inserir
img_add = Image.open('add.png')
img_add = img_add.resize((20,20))
img_add = ImageTk.PhotoImage(img_add)
b_inserir = Button(frameform, image=img_add, width=95, text=" Adicionar", compound=LEFT, anchor=NW, overrelief=RIDGE, font=('Ivy 8'), bg=co1, fg=co0)
b_inserir.place(x=330, y=10)

# Botão Atualizar
img_update = Image.open('update.png')
img_update = img_update.resize((20,20))
img_update = ImageTk.PhotoImage(img_update)
b_update = Button(frameform, image=img_update, width=95, text=" Atualizar", compound=LEFT, anchor=NW, overrelief=RIDGE, font=('Ivy 8'), bg=co1, fg=co0)
b_update.place(x=330, y=50)

# Botão Deletar
img_delete = Image.open('delete.png')
img_delete = img_delete.resize((20,20))
img_delete = ImageTk.PhotoImage(img_delete)
b_delete = Button(frameform, image=img_delete, width=95, text=" Deletar", compound=LEFT, anchor=NW, overrelief=RIDGE, font=('Ivy 8'), bg=co1, fg=co0)
b_delete.place(x=330, y=90)

# Botão Ver Logo
img_logo = Image.open('logo.png')
img_logo = img_logo.resize((20,20))
img_logo = ImageTk.PhotoImage(img_logo)
b_logo = Button(frameform, image=img_logo, width=95, text=" Ver Logo", compound=LEFT, anchor=NW, overrelief=RIDGE, font=('Ivy 8'), bg=co1, fg=co0)
b_logo.place(x=330, y=221)

# Valores das Mensalidades
l_total = Label(frameform, text=" ", width=14, height=2, anchor=CENTER, font=('Ivy 17 bold'), bg=co7, fg=co1)
l_total.place(x=450, y=17)
l_total_ = Label(frameform, text="    Valor Total Mensalidades     ", height=1, anchor=NW, font=('Ivy 10 bold'), bg=co7, fg=co1)
l_total_.place(x=450, y=12)

# Quantidade de Sócios
l_quantidade = Label(frameform, text=" ", width=14, height=2, anchor=CENTER, font=('Ivy 17 bold'), bg=co7, fg=co1)
l_quantidade.place(x=450, y=90)
l_quantidade_ = Label(frameform, text="   Total de Sócios     ", height=1, anchor=NW, font=('Ivy 10 bold'), bg=co7, fg=co1)
l_quantidade_.place(x=450, y=92)


janela.mainloop()
