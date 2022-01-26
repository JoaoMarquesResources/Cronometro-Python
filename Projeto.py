from tkinter import *
import tkinter

cor1 = "#0a0a0a"  # preto
cor2 = "#fafcff"  # branco
cor3 = "#21c25c"  # verde
cor4 = "#eb463b"  # vermelho
cor5 = "#dedcdc"  # Cizento
cor6 = "#3080f0"  # azul

#---------------------------Configurando a Janela-------------------------------

janela = Tk()
#Nome da janela
janela.title("Projeto LTP")
#Comprimento de Largura da janela
janela.geometry('300x180')
#O "bg" é o background
janela.configure(bg=cor1)
#bloquear a propriedade que nos premite alterar as dimensões da janela (durante a execução do programa)
janela.resizable(width=FALSE, height=FALSE)

tempo = "00:00:00"
rodar = False
contador = -5

def iniciar():
    if rodar:
        if contador <= -1:
            #str(contador) para o contador se transformar em string para dar para adicionar ao 'Comecando em: '
            inicio = 'Comecando em: ' + str(contador)




#-------------------------------Criando labels-----------------------------------

#label para adicionar a palavra "Cornômetro" à janela
#text = 'Texto que vai aparecer' / font = ("Tipo de fonte e o tamanho") / bg = cor do background / fg = cor do texto
label_app = Label(janela, text='Cronômetro', font=('Roboto 10'), bg=cor1, fg=cor2)
#aplicar a label na posição x=20 e y=5
label_app.place(x=20, y=5)

#label do tempo / cronômetro
#bold = negrit           text = variavel tempo (que irá aumentar e tal)
label_tempo = Label(janela, text=tempo, font=('Times 50 bold'), bg=cor1, fg=cor4)
label_tempo.place(x=20, y=30)

#--------------------------------Criando Botões----------------------------------

#relief = defenir um estilo para quando o rato clicar / overrelief = defenir um estilo para quando o rato estiver em cima do botão
botao_iniciar = Button(janela, text='Iniciar', font=('Ivy 8 bold'), relief='raised', overrelief='sunken', width=10, height=2, bg=cor1, fg=cor2)
#"criar" o botão
botao_iniciar.place(x=20, y=130)

botao_pausar = Button(janela, text='Pausar', font=('Ivy 8 bold'), relief='raised', overrelief='sunken', width=10, height=2, bg=cor1, fg=cor2)
#"criar" o botão
botao_pausar.place(x=105, y=130)

botao_reiniciar = Button(janela, text='Reiniciar', font=('Ivy 8 bold'), relief='raised', overrelief='sunken', width=10, height=2, bg=cor1, fg=cor2)
#"criar" o botão
botao_reiniciar.place(x=190, y=130)




#Executar/Abrir a janela
janela.mainloop()