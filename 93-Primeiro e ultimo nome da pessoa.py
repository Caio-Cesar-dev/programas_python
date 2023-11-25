"""Exercício Python 027: Faça um programa que leia o nome completo de uma pessoa, mostrando em
seguida o primeiro e o último nome separadamente."""

nome=str(input("Digite o seu nome completo: ")).upper().strip().split()

print("Prazer em conhecê-lo!!")
print("O seu primeiro nome é {} e o seu último nome é {}.".format(nome[0],nome[-1]))