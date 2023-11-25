"""Exercício Python 029: Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma
mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite."""

print()
vel=int(input("Digite a velocidade capturada pelo radar: "))
if vel <= 80:
    print("Tenha um bom dia! dirija com segurança!")
else:
    if vel > 80:
        print("Você foi multado!O limite de 80 km/h foi excedido!")
        print("O valor da multa é de : R$ {:.2f} reais!".format((vel-80)*7))
        print("Tenha cuidado ao dirigir! Segurança sempre!")