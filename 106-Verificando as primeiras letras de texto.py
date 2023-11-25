"""Exercício Python 024: Crie um programa que leia o nome de uma
cidade diga se ela começa ou não com o nome "SANTO"."""

cit=str(input("Digite o nome de uma ciadade: ")).strip().upper()

separa=cit.split()
resul=separa[0]
print(resul=='SANTO')

 #FORMA DA AULA
 #cit=str(input("Digite o nome de uma ciadade: ")).strip()
 #print(cit[:5].upper()=='SANTO')


