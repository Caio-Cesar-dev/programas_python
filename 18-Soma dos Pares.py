"""Exercício Python 50: Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem
 pares. Se o valor digitado for ímpar, desconsidere-o."""
soma=0
cont=0
for i in range(1,7):
    num=int(input("Digite o {}º inteiro: ".format(i)))
    if num % 2 == 0:
        soma += num #funciona como um acumulado r de valores
        cont += 1 # funciona com um contador
        print("Subtotal: ",soma)
print(f" A quantidade de números lido foi: {cont} E a soma dos números PARES foi de:{soma}")