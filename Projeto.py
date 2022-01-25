from tkinter import *
import tkinter

cor1 = "#0a0a0a"  # preto
cor2 = "#fafcff"  # branco
cor3 = "#21c25c"  # verde
cor4 = "#eb463b"  # vermelho
cor5 = "#dedcdc"  # Cizento
cor6 = "#3080f0"  # azul

janela = Tk()
#Nome da janela
janela.title("Projeto LTP")
#Comprimento de Largura da janela
janela.geometry('300x180')
#O "bg" é o background
janela.configure(bg=cor1)
#bloquear a propriedade que nos premite alterar as dimensões da janela (durante a execução do programa)
janela.resizable(width=FALSE, height=FALSE)

#-------------------------------------------Criando labels-------------------------------------------
label_app = Label(janela, text='Cronômetro', font=('Roboto 10'), bg=cor1, fg=cor2)
label_app.place(x=20, y=5)

#Executar/Abrir a janela
janela.mainloop()