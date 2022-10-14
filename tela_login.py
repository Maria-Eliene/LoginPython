from tkinter import * 
from tkinter import Tk, ttk
from tkinter import messagebox 

# ----- Cores 
c0 = "#f0f3f5" # Preto
c1 = "#feffff" # Branco 
c2 = "#3fb5a3" # Verde
c3 = "#38576b" # valor 
c4 = "#403d3d" # Letra

# ----- criando janela 

janela =Tk()
janela.geometry('310x300')
janela.title('')
janela.configure(background='#f0f3f5')
janela.resizable(width=FALSE, height=FALSE)


# ---- dividindo janela 

frame_cima = Frame(janela, width=310,height=50, bg=c1, relief='flat')
frame_cima.grid(row=0, column=0, pady=1, padx=0, sticky=NSEW)

frame_baixo = Frame(janela, width=310,height=250, bg=c1, relief='flat')
frame_baixo.grid(row=1, column=0, pady=1, padx=0, sticky=NSEW)

# ----- configurando o frame cima 
l_nome = Label(frame_cima, text='LOGIN', anchor=NE, font=('Ivy 25 bold'), bg=c1, fg=c4)
l_nome.place(x=5, y=5)

l_linha = Label(frame_cima, text='', width=275, anchor=NW, font=('Ivy 1'), bg=c2, fg=c4)
l_linha.place(x=10, y=45)


credenciais = ['maria','123456789']

# ----- função para verificar os dados do usuário
def verificar_dados():
    usuario = e_usuario.get()
    senha = e_senha.get()

    if usuario == 'admin' and senha == 'admin':
        messagebox.showinfo('Login', 'Seja bem vindo admin!')
    elif credenciais[0] == usuario and credenciais[1] == senha:
        messagebox.showinfo('Login', 'Seja bem vindo(a) ' + credenciais[0])
    else:
        messagebox.showwarning('Erro', 'Dados incorretos!')

# ----- configurando o frame baixo
l_usuario = Label(frame_baixo, text='Usuário *', anchor=NW, font=('Ivy 10'), bg=c1, fg=c4)
l_usuario.place(x=10, y=20)
e_usuario = Entry(frame_baixo, width=25, justify='left', font=("", 15), highlightthickness=1, relief='solid')
e_usuario.place(x=14, y=50)


l_senha = Label(frame_baixo, text='Senha *', anchor=NW, font=('Ivy 10'), bg=c1, fg=c4)
l_senha.place(x=10, y=95)
e_senha = Entry(frame_baixo, width=25, justify='left', show='*',font=("", 15), highlightthickness=1, relief='solid')
e_senha.place(x=14, y=130)


# ----- botão 
b_confirmar = Button(frame_baixo, command=verificar_dados,text='Entrar',width=39,height=2,font=('Ivy 8 bold'), bg=c2, fg=c1, relief=RAISED, overrelief=RIDGE)
b_confirmar.place(x=15, y=180)


janela.mainloop()