"""Exercício Python 53: Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os
espaços. Exemplos de palíndromos:
APOS A SOPA, A SACADA DA CASA, A TORRE DA DERROTA, O LOBO AMA O BOLO, ANOTARAM A DATA DA MARATONA."""

frase=str(input("Digite uma frase: ")).strip().upper()
palavra =frase.split()
junto = ''.join(palavra)
#inverso= junto[::-1] poderiamos fazer dessa forma e eliminar o laço FOR. (linhas 9,10,11) que daria certo e mais simples
inverso=''
for letra in range(len (junto)-1,-1,-1):
    inverso+= junto [letra]
print("O inverso de {} é {} ".format(junto,inverso))
if inverso == junto:
    print("Temos um palíndromo!")
else:
    print("A frese digitada não é um palídromo!")