""" Exercício Python 060: Faça um programa que leia um número qualquer e mostre o seu fatorial. Exemplo:
5! = 5 x 4 x 3 x 2 x 1 = 120"""

"""from math import  factorial
num=int(input("Digite um numero: "))
f=factorial(num)
print(f"O Fatorial de {num} é {f}.")"""

n=int(input("Digite um numero para calcular seu Fatorial: "))
c = n
f = 1
print(f"Calculando {n}! = ", end='')
while c > 0:
    print(f"{c} ", end=' ')
    print('x  ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print(f' {f}')