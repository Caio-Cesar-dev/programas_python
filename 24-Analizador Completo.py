"""Exercício Python 56: Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:
 a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos."""

somaidade=0
mediaidade=0
maioridadehomem=0
nomevelho=0
totmulher=0
for p in range(1,5):
    print("------{}ªPessoa------".format(p))
    nome=str(input("Nome: "))
    idade=int(input("Idade: "))
    sexo=str(input(" Sexo [M/F]: ")).strip().upper()
    somaidade += idade # recebe a idade do grupo
    if p == 1 and sexo in 'M':
        maioridadehomem=idade
        nomevelho=nome
    if sexo in 'M' and idade > maioridadehomem:
        maioridadehomem= idade
        nomevelho = nome
    if sexo in 'F' and idade < 20:
        totmulher += 1
mediaidade =somaidade/4 # vamos obter a media de idade do grupo
print(f"A média de idade do grupo é de {mediaidade} ")
print(f"O homem mais velho tem {maioridadehomem} anos e se chama {nomevelho}")
print(f"Temos ao todo {totmulher} mulherer(s) com menos de 20 anos.")