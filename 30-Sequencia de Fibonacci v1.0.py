"""Exercício Python 63: Escreva um programa que leia um número N inteiro qualquer e mostre na tela
os N primeiros elementos de uma Sequência de Fibonacci. Exemplo:

0 – 1 – 1 – 2 – 3 – 5 – 8"""

print('-'*30)
print("Sequência de Fibonacci ")
print('-'*30)
n=int(input("Informe a quantidade termos que deseja mostrar: "))
t1=0
t2=1
print('~'*30)
print(f"{t1} - {t2}", end='') #ja temos os dois primeiros termos
cont=3  # o contador ja inicia no terceiro termo
while cont <= n:
    t3=t1 + t2
    print(f' - {t3}', end='')
    t1= t2
    t2 =t3
    cont += 1
print(' - Fim')
print('~'*30)