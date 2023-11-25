"""Exercício Python 48: Faça um programa que calcule a soma entre todos os números que são múltiplos de três e que se
encontram no intervalo de 1 até 500."""
soma=0
cont=0
cont2=0
for c in range(1,501,2):
    if c % 3 == 0:
        soma = soma + c
        cont+=1
    cont2 += 1
    print(c,end=' ')
print("\nA soma de todos os multiplus de 3 até 500:Soma= {}".format(soma))
print("A quantidade de números encontrados: ", cont)
print("A quantidade de números ímapares total é de: ", cont2)