"""Exercício Python 42: Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
– EQUILÁTERO: todos os lados iguais
– ISÓSCELES: dois lados iguais, um diferente
– ESCALENO: todos os lados diferentes"""
print('-=-'*10)
print("   Analisador de triângulos")
print('-=-'*10)

r1=float(input("Primeiro segmento: "))
r2=float(input("Segundo segmento: "))
r3=float(input("Terceiro segmento: "))
print('-'*30)
if r1 < r2 +r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print("Os segmentos acima PODEM FORMAR triângulo! ",end='')
    if r1==r2==r3:
        print("Triângulo EQUILÁTERO")
    elif r1 != r2 != r3 != r1:
        print("Triângulo ESCALENO.")
    else:
        print("Triângulo ISOCÉLES.")
else:
    print("Os segmentos acima NÃO PODEM FORMAR triângulo!")

