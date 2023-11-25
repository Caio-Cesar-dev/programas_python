"""Exercício Python 54: Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas
ainda não atingiram a maioridade e quantas já são maiores."""
from datetime import date
age=0

for i in range(1,8):
    ano_nasc=int(input("Informe o ano de nascimento da {}ª pessoa : ".format(i)))
    idade = date.today().year - ano_nasc
    if idade < 18:
        age += 1
        continue

print(f"{age} pessoas ainda Não atingiram a maioridade!!\nE {7 - age} pessoas já são(é) maiores de idade!")
