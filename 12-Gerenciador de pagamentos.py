"""Exercício Python 44: Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço
normal e condição de pagamento:
– à vista dinheiro/cheque: 10% de desconto
– à vista no cartão: 5% de desconto
– em até 2x no cartão: preço formal
– 3x ou mais no cartão: 20% de juros"""
print()
print('{:=^40}'.format(' LOJAS CAIO CÉSAR '))#cetralizado com 40 espaços
print("""FORMAS DE PAGAMENTO 
[1] à vista dinheiro/cheque [10%]
[2] à vista cartão [5%]
[3] 2x no cartão
[4] 3x ou mais no cartão [+20%]""")
print('='*37)
preco=float(input("Digite o valor das compras:R$ "))
f_pgto=int(input("Informe a forma de pagamento: "))
if f_pgto == 1:
    print("O valor das compras foi R${:.2f} com o desconto sai por R$ {:.2f} ".format(preco,(preco-(preco*0.10))))
elif f_pgto == 2:
    print("O valor das compras foi R${:.2f} à vista no cartão sai por R$ {:.2f}".format(preco,(preco-(preco*0.50))))
elif f_pgto == 3:
    print(f"Em duas vezes no cartão não há desconto o preço ficará R$ {preco:.2f}")
elif f_pgto == 4:
    num_parcelas=int(input("Em quantas parcelas deseja dividir: "))
    total=preco+(preco*0.20)
    total_div=total/num_parcelas
    print(f" {num_parcelas} Parcelas")
    print("O valor de R$ {:.2f} sairá no total de R$ {:.2f} ".format(preco,total))
    print(f"Cada parcela será de R$ {total_div:.2f}")
else:
    print("\033[1;31m OPCÃO INVALIDA, TENTE NOVAMENTE!! ")