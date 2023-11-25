"""Exercício Python 58: Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10. Só que
 agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer."""

from random import randint
from time import sleep


print('-=-' * 20)
nome=str(input("Qual o seu nome: ")).upper()
print(f"Olá, {nome}!! \nEu sou o Mr Robbot. ")
print("Vou pensar em um número entre 0 e 10. Tente adivinhar!!")
print("-=-" * 20)
computador=999 #coloquei este número apenas para iniciar o loop
jogador=''
palpite=0
while jogador != computador:
    computador = randint(0, 10)  # faz o computador escolher entre o inicio e fim dos numeros
    jogador= int(input("Em que número eu pensei? Digite o número: "))#jogador tenta advinhar
    print("PROCESSADO...")
    palpite+= 1
    sleep(1)#processa por um tempo... da a impressao de que a maquina está pensando na resposta
    if jogador == computador:
        print(f"PARABÊNS {nome}! Você conseguiu me vencer! Você precisou de {palpite} palpites!")
    else:
        print(f"_MR Robot: GANHEI! Eu pensei no número {computador} e não no numero {jogador} ")
        print("Tente novamente!!!")