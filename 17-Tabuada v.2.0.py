"""Exercício Python 49: Refaça o DESAFIO 9, mostrando a tabuada de um número que o usuário escolher, só que
agora utilizando um laço for."""
print("Qual número você gostaria de obter a tabuada?")
num=int(input("Digite um numero de 0 a 10: "))
for valor in range(-1,10,1):
    valor += 1
    print(f"{num} x {valor}= {num*valor}")