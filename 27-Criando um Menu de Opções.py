"""Exercício Python 059: Crie um programa que leia dois valores e mostre um menu na tela:
[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] divisão
[ 5 ] sair do programa
Seu programa deverá realizar a operação solicitada em cada caso."""


print("""[1] Somar\n[2] Multiplicar\n[3] Maior\n[4] Divisão\n[5] Sair do Programa""")

user= 0
while user !=5 :
    print("-="*20)
    print("Olá o que gostaria de fazer? ")
    cod=int(input("Digite a opção: "))
    if cod == 1:
        soma1 = float(input("Digite o primeiro número: "))
        soma2 = float(input("Digite o segundo número: "))
        print(f"O resultado da soma entre {soma1} + {soma2} = {soma1+soma2}")
    if cod == 2:
        mult1 = float(input("Digite o primeiro número: "))
        mult2 = float(input("Digite o segundo número: "))
        print(f"O resultado da multiplicação entre {mult1} x {mult2} = {mult1*mult2}")
    if cod == 3:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        if num1 > num2:
            print(f"O numero {num1} é maior que {num2}.")
        else:
            num2 > num1
            print(f"O numero {num2} é maior que {num1}.")
    if cod == 4:
        div1 = float(input("Digite o primeiro número: "))
        div2 = float(input("Digite o segundo número: "))
        print(f"O resultado da divisão entre {div1} / {div2} = {div1/div2}")
    if cod == 5:
        print("Sair!")
        break
    if cod > 5:
        print("Opção invalida!! Tente novamente!!")