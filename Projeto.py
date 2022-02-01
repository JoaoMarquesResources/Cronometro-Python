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

#---------------------------Funções dos botões-------------------------------

#definindo variaveis globais (para ser possivel usar as funções dentro e fora das funções e do programa / em todo o programa)
global tempo
global rodar
global contador
global limitador
global executar
global PodeReiniciar

PodeReiniciar = False
executar = True
limitador = 59
tempo = "00:00:00"
rodar = False
contador = -5


#função iniciar
def iniciar():
    global tempo
    global contador
    global limitador
    global PodeReiniciar
    tempo = "00:00:00"
    #Se a variavel rodar = true (está em False) irá ficar True na função start() e irá ficar False na função de pausar()
    if rodar:
        #Se o contador for menor ou igual a -1 (o contador começa em -5)
        #Antes do cronometro começar
        if contador <= -1:
            PodeReiniciar = False
            #str(contador) para o contador se transformar em string para dar para adicionar ao 'Comecando em: '
            inicio = 'Comecando em: ' + str(contador)
            #Dizer que o texto do tempo vai ser = à variavel inicio
            label_tempo['text'] = inicio
            #Dizer que a fonte do tempo vai ser = Roboto 12
            label_tempo['font'] = 'Roboto 12'
            #Dizer que o fg do tempo vai ser = à cor
            label_tempo['fg'] = cor4
        #Começando o cronometro
        else:
            PodeReiniciar = True
            label_tempo['font'] = 'Times 50 bold'

            temporario = str(tempo)
            #o map vai scanear a variável temporario e quando encontrar o ":" ele vai separar o 00 assim fica h = 00 (primeiros 00), m = 00 (segundos 00), s = 00 (terceiros 00) 
            h, m, s = map(int, temporario.split(":"))
            h = int(h) #transformar a string em int
            m = int(m)
            s = int(contador)

            #Se os segundos chegarem a 59
            if s >= limitador:
                #resetar o contador
                contador = 0
                #Aumentar o numero de minutos
                m += 1
                #Se os minutos forem = 60
                if m == 60:
                    #Aumenta a hora
                    h += 1
                    #Reseta os minutos
                    m = 0
            
            s = str(0) + str(s)
            m = str(0) + str(m)
            h = str(0) + str(h)

            #Atualizando os valores
            #temporario vai voltar ao formato 00:00:00
            #h[-2] é para pegar os dois ultimos characteres da string
            temporario = str(h[-2:]) + ":" + str(m[-2:]) + ":" + str(s[-2:])
            label_tempo['text'] = temporario
            tempo = temporario


        # after (depois) de 1000 milisegundos (1 segundo) executa o iniciar()
        label_tempo.after(1000, iniciar)
        contador += 1


#função start para dar inicio à função iniciar
def start():
    global rodar
    global executar
    #Dizer que a variavel rodar = True para que o if rodar: na função iniciar() consiga ser executado
    #este if serve para certificar que não se pode spamar o iniciar
    if executar == True:
        rodar = True
        #executando a função iniciar
        iniciar()
        executar = False

#função do botão pausar
def pausar():
    global rodar
    global executar
    #Se dizermos que o rodar é = False estamos a parar o cronometro porque ele só "roda" se for True (ver isso na função iniciar)
    executar = True
    rodar = False

#função reiniciar
def reiniciar():
    global tempo
    global contador
    global PodeReiniciar

    if PodeReiniciar == True:
        #reiniciando o contador e o tempo
        contador = 0
        tempo = "00:00:00"
        label_tempo['text'] = tempo

#----------------------------Criando labels--------------------------------

#label para adicionar a palavra "Cornômetro" à janela
#text = 'Texto que vai aparecer' / font = ("Tipo de fonte e o tamanho") / bg = cor do background / fg = cor do texto
label_app = Label(janela, text='Cronômetro', font=('Roboto 10'), bg=cor1, fg=cor2)
#aplicar a label na posição x=20 e y=5
label_app.place(x=20, y=5)

#label do tempo / cronômetro
#bold = negrit           text = variavel tempo (que irá aumentar e tal)
label_tempo = Label(janela, text=tempo, font=('Times 50 bold'), bg=cor1, fg=cor4)
label_tempo.place(x=20, y=30)

#------------------------------Criando Botões-------------------------------

#command = função que irá executar quando o botão for clicado / relief = defenir um estilo para quando o rato clicar / overrelief = defenir um estilo para quando o rato estiver em cima do botão
botao_iniciar = Button(janela, command=start, text='Iniciar', font=('Ivy 8 bold'), relief='raised', overrelief='sunken', width=10, height=2, bg=cor1, fg=cor2)
#"criar" o botão
botao_iniciar.place(x=20, y=130)

botao_pausar = Button(janela, command=pausar, text='Pausar', font=('Ivy 8 bold'), relief='raised', overrelief='sunken', width=10, height=2, bg=cor1, fg=cor2)
#"criar" o botão
botao_pausar.place(x=105, y=130)

botao_reiniciar = Button(janela, command=reiniciar, text='Reiniciar', font=('Ivy 8 bold'), relief='raised', overrelief='sunken', width=10, height=2, bg=cor1, fg=cor2)
#"criar" o botão
botao_reiniciar.place(x=190, y=130)


#Executar/Abrir a janela
janela.mainloop()