"""Exercício Python 39: Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua
idade, se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do
alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo."""

from datetime import date
ano=int(input("Infome o seu ano de nascimento: "))
ano_atual= date.today().year # busca o ano atual em que a máquina esta configurada
idade= ano_atual-ano

if idade == 18:
    print("Tempo exato de alistamento!")
elif idade < 18:
    print("Ainda faltam {} anos pro alistamento!".format(18-idade))
    print("Seu alistamento será em {} ".format(ano_atual+(18-idade)))
elif idade > 18:
    print("Você já passou {} anos do tempo de alistamento!!!".format(idade-18))