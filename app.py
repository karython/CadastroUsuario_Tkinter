from tkinter import *
import services

def main():
    def on_enviar():
        nome = nomeEntry.get()
        email = emailEntry.get()
        cpf = cpfEntry.get()
        services.enviar_dados(nome, email, cpf)

        # Para limpar os campos apos a insercao
        nomeEntry.delete(0, END)
        emailEntry.delete(0, END)
        cpfEntry.delete(0, END)

    janela = Tk()
    janela.title("Formulario")
    janela.geometry("400x300")

    titulo = Label(janela, text='CRUD', font=('Arial', 20))
    titulo.pack(pady=30)

    nome = Label(janela, text="Nome:")
    nome.place(x=50, y=100)

    global nomeEntry
    nomeEntry = Entry(janela, width=30)
    nomeEntry.place(x=100, y=100)

    email = Label(janela, text="Email:")
    email.place(x=50, y=130)

    global emailEntry
    emailEntry = Entry(janela, width=30)
    emailEntry.place(x=100, y=130)

    cpf = Label(janela, text="CPF:")
    cpf.place(x=50, y=160)

    global cpfEntry
    cpfEntry = Entry(janela, width=30)
    cpfEntry.place(x=100, y=160)

    enviar = Button(janela, text="Enviar", width=10, command=on_enviar)
    enviar.place(x=100, y=200)

    janela.mainloop()

if __name__ == '__main__':
    main()