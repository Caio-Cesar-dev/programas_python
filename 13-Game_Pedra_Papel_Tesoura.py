"""Exercício Python 45: Crie um programa que faça o computador jogar Jokenpô com você."""
from random import randint
from time import sleep
print("""Suas Opções:
[1] PEDRA
[2] PAPEL
[3] TESOURA""")
jogador=int(input("Qual a sua jogada? "))
print('-='*15)
print("JO")
sleep(1)
print("KEN")
sleep(1)
print("PO!!!")
computer=randint(1,3)

if (jogador == 1 and computer == 1) or (jogador==2 and computer==2) or (jogador==3 and computer==3):
    print("EMPATE, os dois fizeram a mesma escola")
elif jogador == 1 and computer == 2:
    print("O computador jogou PAPEL e você PEDRA")
    print("PAPEL cobre PEDRA")
    print("\033[1;31m Você PERDEU !")
elif jogador == 1 and computer == 3:
    print("Você jogou PEDRA e o computador jogou TESOURA")
    print("PEDRA quebra TESOURA!")
    print("\033[1;34m Você VENCEU!")
elif jogador == 2 and computer == 1:
    print("você jogou papel e o computador jogou PEDRA")
    print("PAPEL cobre PEDRA")
    print("\033[1;34m Você VENCEU!")
elif jogador == 2 and computer == 3:
    print("Você jogou PAPEL e o computador jogou TESOURA")
    print("TESOURA corta PAPEL")
    print("\033[1;31m Você PERDEU!")
elif jogador == 3 and computer == 1:
    print("Você jogou TESOURA e computador jogou PEDRA")
    print("PEDRA quebra TESOURA")
    print("\033[1;31m Você PERDEU")
elif jogador == 3 and computer == 2:
    print("Você jogou TESOURA e computador jogou PAPEL")
    print("TESOURA corta PAPEL!")
    print("\033[1;34m Você VENCEU!")

print('-='*15)