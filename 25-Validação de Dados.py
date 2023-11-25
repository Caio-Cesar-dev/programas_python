"""Exercício Python 57: Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’. Caso esteja
errado, peça a digitação novamente até ter um valor correto."""

sexo=str(input("Digite o sexo [M/F]: ")).strip().upper()
while sexo not in 'MF':
    sexo = str(input("Dados Invalidos!!! Digite o sexo novamente ![M/F]: ")).strip().upper()
    print("Digite corretamente.")
print(f"Dados recebidos com suceso! Você digitou {sexo}")