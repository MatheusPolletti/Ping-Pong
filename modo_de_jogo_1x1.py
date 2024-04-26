from tkinter import *
from time import sleep
from random import uniform, randint

def jogo_real(funcao):
    def wrappper():

        def fim(event):
            apresentacao.destroy()

        apresentacao = Tk()

        apresentacao.title('Ping Pong Polletti')
        icone = PhotoImage(file='ícone.png')
        apresentacao.iconphoto(True, icone)

        apresentacao.geometry('420x400')
        apresentacao.config(bg='#FFCB39')

        criador = Label(apresentacao, text='Desenvolvido por Matheus Polletti', bg='#FFCB39', fg='black', font=('SF UI Display Regular', 12))
        criador.place(x = 177, y = 375)

        anuncio = Label(apresentacao, text='Prepare-se para jogar!!', bg='#FFCB39', fg='black', font=('Bungee Shade', 16))
        anuncio.place(x = 110, y = 120)

        botao = Label(apresentacao, text='Cliques na tela para começar', bg='#FFCB39', fg='black', font=('Bungee Shade', 16))
        botao.place(x = 80, y = 170)

        apresentacao.bind('<Button-1>', fim)

        apresentacao.mainloop()

        funcao()

    return wrappper()


@jogo_real
def modo_1x1():
    def mover_cima(event):
        if jogador_1.winfo_y() > 0:
            jogador_1.place(x = jogador_1.winfo_x(), y=jogador_1.winfo_y() - 10)


    def mover_baixo(event):
        if jogador_1.winfo_y() < 340:
            jogador_1.place(x = jogador_1.winfo_x(), y = jogador_1.winfo_y() + 10)


    def mover_cima_rapido(event):
        if jogador_2.winfo_y() > 0:
            jogador_2.place(x = jogador_2.winfo_x(), y=jogador_2.winfo_y() - 10)


    def mover_baixo_rapido(event):
        if jogador_2.winfo_y() < 340:
            jogador_2.place(x = jogador_2.winfo_x(), y = jogador_2.winfo_y() + 10)


    jogo = Tk()

    jogo.title('Ping Pong Polletti')
    icone = PhotoImage(file='ícone.png')
    jogo.iconphoto(True, icone)

    imagem = PhotoImage(file='imagem.png')

    jogo.bind('<w>', mover_cima)
    jogo.bind('<s>', mover_baixo)
    jogo.bind('<Up>', mover_cima_rapido, add='+')
    jogo.bind('<Down>', mover_baixo_rapido, add='+')

    jogo.geometry('420x400')
    jogo.config(bg='black')

    jogador_1 = Label(jogo, image=imagem, width=1.5, height=55)
    jogador_1.place(x = 40, y = 170)

    jogador_2 = Label(jogo, image=imagem, width=1.5, height=55)
    jogador_2.place(x = 375, y = 170)

    bola = Label(jogo, image=imagem, width=4, height=4)

    movimento_x = 200
    movimento_y = 200

    while True:
        velocidade_movimento_x = randint(-2, 2)
        if velocidade_movimento_x == 0:
            continue
        break
    velocidade_movimento_y = 1
    
    acertos = 0
    cont = 0

    while True:

        bola.place(x =  movimento_x, y = movimento_y)
        jogo.update()

        movimento_x += velocidade_movimento_x
        movimento_y += velocidade_movimento_y

        if movimento_x > 411:
            perdedor = 'O jogador 1 venceu.\n\n\nO jogador 2 perdeu'
            break
        if movimento_x <= 0:
            perdedor = 'O jogador 2 venceu.\nO jogador 1 perdeu'
            break

        if movimento_y > 391 or movimento_y < 0:
            velocidade_movimento_y = -velocidade_movimento_y

        if movimento_x == jogador_1.winfo_x():
            if movimento_y + 10 > jogador_1.winfo_y():
                if movimento_y - 60 < jogador_1.winfo_y():
                    velocidade_movimento_x = -velocidade_movimento_x
                    acertos += 1
                    velocidade_movimento_y = round(uniform(0.1, 1.1), 1)

        if movimento_x == jogador_2.winfo_x() - 4:
            if movimento_y + 10 > jogador_2.winfo_y():
                if movimento_y - 60 < jogador_2.winfo_y():
                    velocidade_movimento_x = -velocidade_movimento_x
                    acertos += 1
                    velocidade_movimento_y = round(uniform(0.1, 1.1), 1)
        
        sleep(0.01)

    jogador_1.destroy()
    jogador_2.destroy()
    perdeu = Label(jogo, text=perdedor, bg='black', fg='blue', font=('Bungee Shade', 12))
    perdeu.place(x = 140, y = 130)

    #sleep(3)
    #jogo.destroy()

    jogo.mainloop()


#modo_1x1()
