from tkinter import *
from time import sleep
from random import uniform

def infinito():
    def mover_cima(event):
        if jogador.winfo_y() > 0:
            jogador.place(x = jogador.winfo_x(), y=jogador.winfo_y() - 5)


    def mover_baixo(event):
        if jogador.winfo_y() < 265:
            jogador.place(x = jogador.winfo_x(), y = jogador.winfo_y() + 5)


    def mover_cima_rapido(event):
        if jogador.winfo_y() > 0:
            jogador.place(x = jogador.winfo_x(), y=jogador.winfo_y() - 10)


    def mover_baixo_rapido(event):
        if jogador.winfo_y() < 265:
            jogador.place(x = jogador.winfo_x(), y = jogador.winfo_y() + 10)


    jogo = Tk()

    jogo.title('Ping Pong Polletti')
    icone = PhotoImage(file='ícone.png')
    jogo.iconphoto(True, icone)

    imagem = PhotoImage(file='imagem.png')

    jogo.bind('<w>', mover_cima)
    jogo.bind('<s>', mover_baixo)
    jogo.bind('<Up>', mover_cima_rapido)
    jogo.bind('<Down>', mover_baixo_rapido)

    jogo.geometry('320x320')
    jogo.config(bg='black')

    jogador = Label(jogo, image=imagem, width=1.5, height=55)
    jogador.place(x = 40, y = 120)

    bola = Label(jogo, image=imagem, width=4, height=4)

    movimento_x = 150
    movimento_y = 150
    velocidade_movimento_x = 1
    velocidade_movimento_y = round(uniform(0.1, 1.1),1)

    acertos = 0

    while True:
        bola.place(x =  movimento_x, y = movimento_y)
        jogo.update()
        movimento_x += velocidade_movimento_x
        movimento_y += velocidade_movimento_y
        if movimento_x > 312:
            velocidade_movimento_x = -velocidade_movimento_x
        if movimento_y > 312 or movimento_y < 0:
            velocidade_movimento_y = -velocidade_movimento_y
        if movimento_x == jogador.winfo_x():
            if movimento_y + 10 > jogador.winfo_y():
                if movimento_y - 60 < jogador.winfo_y():
                    velocidade_movimento_x = -velocidade_movimento_x
                    acertos += 1
                    velocidade_movimento_y = round(uniform(0.1, 1.1), 1)
        if movimento_x <= 0:
            break
        sleep(0.007)

    jogador.destroy()
    perdeu = Label(jogo, text=f'Infelizmente você perdeu.\nVocê conseguiu se defender {acertos} vezes.', bg='black', fg='blue', font=('Bungee Shade', 12))
    perdeu.place(x = 40, y = 130)

    jogo.mainloop()

infinito()
