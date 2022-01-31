teste = True

#enquanto teste é diferente de False que é True
while teste != False:
    resposta = int(input("Se digitar o número 0, o programa irá parar: "))

    if resposta == 0:
        #podes fazer um break para parar o loop
        break
        #ou podes por a variavel teste para False (irá parar o loop pq é while o teste for True)
        teste = False
