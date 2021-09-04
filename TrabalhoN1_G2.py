'''
    Técnicas de Programação
-Atividade N1 - Parte

Grupo 2:
Nome:   Rafael Henrique Gonçalves Soares    RA: 21566288
Nome:   Paulo Henrique Augusto              RA: 21532508
Nome:   Gustavo Mello Soares dos Santos     RA: 21568663
Nome:   Gabriel de Souza Alves              RA: 21587787
'''

#   Importação das bibliotecas
import random

#Declaração de variáveis: Antes do Início do programa é necessário declarar algumas variáveis essenciais

caminho = 0     #É a variável responsável por guardar o caminho escolhido, inicializada em 0. Os caminhos vermelho e preto serão selecionados respectivamente por "1" e "2"
sala = 1        #É a variável responsável por guardar a sala que a Guilda (Usuário) está no momento. Inicializada na sala de valor "1"
interacao = 0   #Variavel relativa à quantidade de interações, iniciada em "0". Ela será responsável por guardar a quantidade total de movimentos/interações para "vencer" esse labirinto

#Inicio do Programa
while (1):  #Laço de repetição do inicio do programa
    if (sala == 9) and (interacao <7):  #Verificação do número de salas, se for igual a 9 com menos de 7 interações, o jogador vence
        print("\nParabéns você chegou ao fim do labirinto com {} interações, Vc e sua Guilda Venceram o Labirinto !!!".format(interacao))
        break
    else:   #Execução do programa, onde o usuário vai selecionar o caminho que vai percorrer
        print ("Você está na sala: {}".format(sala))    
        print ("Escolha seu caminho: ")
        print ("[1] - Caminho vermelho")
        print ("[2] - Caminho caminho preto")
        caminho = int(input())
else:
    print("Você se Perdeu no labirinto para todo o sempre buahahahahahahahaha !") # Easter-egg no Código