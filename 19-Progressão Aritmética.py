"""Exercício Python 51: Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os
10 primeiros termos dessa progressão."""
print('='*25)
print("   10 TERMOS DE UMA PA")
print('='*25)

primeiro=int(input("Informe o primeiro termo: "))
razao=int(input("Informe a RAZÃO: "))
decimo=primeiro+(10-1)*razao # formula p/ o N-énesimo termo de uma PA (an = a1 + (n – 1) . r)

for c in range(primeiro,decimo + razao,razao):
    print("{} ".format(c),end='► ')
print("Acabou!")