import random
from tkinter import *
from tkinter import ttk

# Cores
co0 = '#000000'  # preta
co1 = '#feffff' # branca
co2 = '#6f9fbd'  # azul
co3 = '#38576b'  # valor
co4 = '#403d3d'  # letra
co5 = '#e06636'  # - profit
co6 = '#6dd695'  # + profit
co7 = '#ef5350'  # vermelha
co8 = '#00bfa5'  # + verde
fundo = '#3b3b3b'
co10 = '#fcfbf7'
cor1 = '#f58b5d'
cor2 = '#ff333a'
cor3 = '#6bd66f'
cor4 = '#ab8948'

janela = Tk()
janela.title('')
janela.geometry('350x280')
janela.configure(bg=fundo)

# Frames
ttk.Separator(janela, orient=HORIZONTAL).grid(row=0, columnspan=2, ipadx=280)

frame_top = Frame(janela, width=350, height=30, bg=co1, pady=0, padx=0, relief="flat")
frame_top.grid(row=1, column=0, sticky=NW)

frame_corpo = Frame(janela, width=350, height=280, bg=fundo, pady=0, padx=0, relief="flat")
frame_corpo.grid(row=2, column=0, sticky=NW)

estilo = ttk.Style(janela)
estilo.theme_use("clam")

# ------------------------------------------- Função iniciar jogo ------------------------------------------------------------
tentativas = 5
pontuacao = 0

def iniciar_jogo():
    layout_regra_1['text'] = ''
    layout_regra_2['text'] = ''
    layout_regra_3['text'] = ''

    numeros = random.sample(range(1, 10),8)
    random.choice(numeros)
    

    def estado_do_valor(v):

        numeros1 = random.sample(range(1, 10), 8)
        resposta = [random.choice(numeros1)]

        global tentativas
        global pontuacao

        for i in resposta:
            if v == i:
                tentativas += 2
                pontuacao += 10
                layout_tentativas['text'] = f'Tentativas: {tentativas}'
                layout_pontuacao['text'] = f'Pontuação: {pontuacao}'

            else:
                tentativas -= 1
                layout_tentativas['text'] = f'Tentativas: {tentativas}'

                # Desabilitar botões, se tentativas for igual a 0
                if tentativas == 0:
                    botao_1['state'] = DISABLED
                    botao_2['state'] = DISABLED
                    botao_3['state'] = DISABLED
                    botao_4['state'] = DISABLED
                    botao_5['state'] = DISABLED
                    botao_6['state'] = DISABLED
                    botao_7['state'] = DISABLED
                    botao_8['state'] = DISABLED

                    botao_1['text'] = ""
                    botao_2['text'] = ""
                    botao_3['text'] = ""
                    botao_4['text'] = ""
                    botao_5['text'] = ""
                    botao_6['text'] = ""
                    botao_7['text'] = ""
                    botao_8['text'] = ""

                    # Chamar a função game_over
                    game_over()

                else:
                    pass

    botao_1 = Button(frame_corpo, command=lambda:estado_do_valor(numeros[0]), text= numeros[0], width=4, height=2, font='ivy 15 bold', bg=co10, fg=co0, relief=RAISED, overrelief=RIDGE) # type: ignore
    botao_1.place(x=39, y=70)

    botao_2 = Button(frame_corpo, command=lambda:estado_do_valor(numeros[1]), text= numeros[1], width=5, height=2, font='ivy 15 bold', bg=co10, fg=co0, relief=RAISED, overrelief=RIDGE) # type: ignore
    botao_2.place(x=108, y=70)

    botao_3 = Button(frame_corpo, command=lambda:estado_do_valor(numeros[2]), text= numeros[2], width=5, height=2, font='ivy 15 bold', bg=co10, fg=co0, relief=RAISED, overrelief=RIDGE) # type: ignore
    botao_3.place(x=176, y=70)

    botao_4 = Button(frame_corpo, command=lambda:estado_do_valor(numeros[3]), text= numeros[3], width=4, height=2, font='ivy 15 bold', bg=co10, fg=co0, relief=RAISED, overrelief=RIDGE) # type: ignore
    botao_4.place(x=244, y=70)

    botao_5 = Button(frame_corpo, command=lambda:estado_do_valor(numeros[4]), text= numeros[4], width=4, height=2, font='ivy 15 bold', bg=co10, fg=co0, relief=RAISED, overrelief=RIDGE) # type: ignore
    botao_5.place(x=39, y=130)

    botao_6 = Button(frame_corpo, command=lambda:estado_do_valor(numeros[5]), text= numeros[5], width=5, height=2, font='ivy 15 bold', bg=co10, fg=co0, relief=RAISED, overrelief=RIDGE) # type: ignore
    botao_6.place(x=108, y=130)

    botao_7 = Button(frame_corpo, command=lambda:estado_do_valor(numeros[6]), text= numeros[6], width=5, height=2, font='ivy 15 bold', bg=co10, fg=co0, relief=RAISED, overrelief=RIDGE) # type: ignore
    botao_7.place(x=176, y=130)

    botao_8 = Button(frame_corpo, command=lambda:estado_do_valor(numeros[7]), text= numeros[7], width=4, height=2, font='ivy 15 bold', bg=co10, fg=co0, relief=RAISED, overrelief=RIDGE) # type: ignore
    botao_8.place(x=244, y=130)

    
def game_over():
    global tentativas
    global pontuacao

    layout_pontuacao1 = Label(frame_corpo, text=f'Voçê fez {pontuacao} pontos!', relief='raised', anchor='center', font='ivy 12 bold', bg=co0, fg=co1)
    layout_pontuacao1.place(x=104, y=90)

    layout_jogo = Label(frame_corpo, text='GAME OVER', relief='raised', anchor='center', font='ivy 14 bold', bg=co0, fg=co1)
    layout_jogo.place(x=120, y=150)

    tentativas = 5
    pontuacao = 0

    layout_tentativas['text'] = f'Tentativas: {tentativas}'
    layout_pontuacao['text'] = f'Pontuação: {pontuacao}'

    botao_jogar1 = Button(frame_corpo, command=iniciar_jogo, text='JOGAR NOVAMENTE', width=17, font='ivy 8 bold', bg=co10, fg=co0, relief=RAISED, overrelief=RIDGE)
    botao_jogar1.place(x=112, y=210)



# ------------------------------------------- Configurações frame_top --------------------------------------------------------
app_nome = Label(frame_top, text='ADIVINHE O NÚMERO', anchor='center', font='ubuntu 14 bold', bg=co1, fg=co3)
app_nome.place(x=70, y=0)

# ------------------------------------------ Configurações frame_corpo ------------------------------------------------------
layout_pontuacao = Label(frame_corpo, text='Pontuação: 0', anchor='center', font='ivy 11 bold', bg=fundo, fg=co1)
layout_pontuacao.place(x=40, y=15)

layout_tentativas = Label(frame_corpo, text='Tentativas: 5', anchor='center', font='ivy 11 bold', bg=fundo, fg=co1)
layout_tentativas.place(x=220, y=15)

layout_barra = Label(frame_corpo, text='', width=91, anchor='center', font='ivy 4', bg=cor3, fg=co7)
layout_barra.place(x=39, y=59)

layout_regra_1 = Label(frame_corpo, text='Tente adivinhar o número para pontuar.', anchor='center', font='ivy 8 bold', bg=fundo, fg=co1)
layout_regra_1.place(x=50, y=80)

layout_regra_2 = Label(frame_corpo, text='Se voçê acertar, voçê ganhará mais 2 chances!', anchor='center', font='ivy 8 bold', bg=fundo, fg=co1)
layout_regra_2.place(x=50, y=100)

layout_regra_3 = Label(frame_corpo, text='Se voçê errar, as suas chances irão reduzir!', anchor='center', font='ivy 8 bold', bg=fundo, fg=co1)
layout_regra_3.place(x=50, y=120)

botao_jogar = Button(frame_corpo, command=iniciar_jogo, text='JOGAR', width=40, font='ivy 8 bold', bg=co10, fg=co0, relief=RAISED, overrelief=RIDGE)
botao_jogar.place(x=40, y=170)


janela.mainloop()
