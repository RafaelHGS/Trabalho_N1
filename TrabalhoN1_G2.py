'''
    Técnicas de Programação
-Atividade N1 - Parte

Grupo 2:
Nome:   Rafael Henrique Gonçalves Soares    RA: 21566288
Nome:   Paulo Henrique Augusto              RA: 21532508
Nome:   Gustavo Mello Soares dos Santos     RA: 21568663
Nome:   Gabriel de Souza Alves              RA: 21587787
'''

import random

caminho = 0     
sala = 1        
interacao = 0   


while (1):
    if (sala == 9) and (interacao <7):
        print("\nParabéns você chegou ao fim do labirinto com {} interações, Vc e sua Guilda Venceram o Labirinto !!!".format(interacao))
        break
    elif (sala == 9) and (interacao >= 7):
        print("\n\tInfelizmente Você se Perdeu no meio do caminho e levou\n mais do que 7 interações para chegar na sala 9")
        print ("Tente novamente com menos movimentos/interações, e Boa Sorte!")
        print ("Total de Interações/Movimentos: {}".format(interacao))
        break
    else:
        print ("Você está na sala: {}".format(sala))    
        print ("Escolha seu caminho: ")
        print ("[1] - Caminho vermelho")
        print ("[2] - Caminho preto")
        caminho = int(input())

        while (caminho <= 0) or (caminho >= 3):
            print("\nSem trapacear !\n Você Deve escolher um caminho 'vermelho' ou 'preto' para prosseguir !\n")
            print ("Você está na sala: {}".format(sala))    
            print ("Escolha seu caminho: ")
            print ("[1] - Caminho vermelho")
            print ("[2] - Caminho preto")
            caminho = int(input())
        else:
            while (caminho == 1):
                interacao = interacao + 1
                if (sala == 6):
                    print ("\nVocê está na sala: {}, pórem aqui só existe um caminho que o leva para a sala 8".format(sala))
                    print ("Portanto, vc segue esse caminho que te leva para a sala 8\n")
                    sala = 8
                    caminho = 0
                else:
                    sala = sala + 1
                    caminho = 0  
