from tkinter import *
#from modo_de_jogo_infinito import infinito
#import modo_de_jogo_1x1

def jogar_infinito():
   #infinito()
   pass


def jogar_1x1():
    #modo_de_jogo_1x1.modo_1x1()
    pass


def sair():
    quit()


if __name__ == '__main__':
    janela = Tk()

    janela.title('Ping Pong Polletti')
    icone = PhotoImage(file='ícone.png')
    janela.iconphoto(True, icone)

    frame_opcoes = Frame(janela)
    frame_opcoes.place(x = 195, y = 150)

    janela.geometry('500x500')
    janela.config(bg='#FFCB39')

    texto_ping_pong = Label(janela, text='Ping Pong Polletti', bg='#FFCB39', font=('SF UI Display Black', 22))
    texto_ping_pong.place(x = 140, y = 0)

    botao_jogar_modo_infinito = Button(frame_opcoes, text='Modo Infinito', bg='black', fg='white', width=10, bd=5, font=('Bungee Shade', 16), command=jogar_infinito).pack()

    botao_jogar_modo_1x1 = Button(frame_opcoes, text='Modo 1x1', bg='black', fg='white', bd=5, width=10, font=('Bungee Shade', 16), command=jogar_1x1).pack()

    botao_sair = Button(frame_opcoes, text='Sair', bg='black', fg='white', width=10, bd=5, font=('Bungee Shade', 16), command=sair).pack()

    texto_criador = Label(janela, text='Criado por Matheus Polletti', bg='#FFCB39', font=('SF UI Display Regular', 12)).place(x = 300, y = 475)

    janela.mainloop()
