"""Exercício Python 43: Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de
Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:
– IMC abaixo de 18,5: Abaixo do Peso
– Entre 18,5 e 25: Peso Ideal
– 25 até 30: Sobrepeso
– 30 até 40: Obesidade
– Acima de 40: Obesidade Mórbida"""
alt=float(input("Digite a sua altura: (m)"))
peso=float(input("Digite seu peso: (Kg)"))
imc=peso/(alt*alt)
print('-=-'*30)
if imc < 18.5:
    print(f"IMC {imc:.1f}Seu peso está abaixo do peso NORMAL.")
if imc >=18.5 and imc <25:
    print(f"IMC {imc:.1f} Parabéns seu peso está ideal!!")
elif imc > 25 and imc < 30:
    print(f"IMC {imc:.1f} Cuidado! Já está com sobrepeso!!!")
elif imc > 30 and imc < 40:
    print(f"IMC {imc:.1f} Você está obeso!!!!")
elif imc > 40 :
    print(f"\033[1;31m IMC {imc:.1f} Tá lascado ...Obesidade Morbida!!!!")