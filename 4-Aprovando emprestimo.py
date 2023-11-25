"""Exercício Python 36: Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o
valor da casa, o salário do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do
salário ou então o empréstimo será negado."""

valor_casa=float(input("Qual o valor do imóvel: "))
sal=float(input("Qual o salário: "))
tempo=int(input("Em quantos anos pretende pagar: "))
prest_mesal= valor_casa/(tempo*12)

if prest_mesal > (sal * 0.30):
    print("\033[1;31m Espretimo Negado !!")
    print(f"\033[1;31m A prestação de R$ {prest_mesal:.2f} excede mais de 30 porcento do salário!!! ")
else:
    print(f"\033[1;34m O emprestimo foi APROVADO, a prestação será de R$ {prest_mesal:.2f}.!!")