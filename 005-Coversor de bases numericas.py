"""Exercício Python 37: Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher
qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal."""

num=int(input("Digite um número inteiro: "))
print('''Escolha uma das BASES para a converssão:
[1] converter para BINARIO
[2] converter para OCTAL
[3] converter para HEXADECIMAL''')
print('-=-'*25)
opcao=int(input("Digite a sua opção: "))
if opcao == 1:
    print("{} convertido para BINÁRIO é igual a: {}".format(num,bin(num)[2:]))
elif opcao==2:
    print("{} convertido para OCTAL é igual a: {}".format(num,oct(num)[2:]))
elif opcao==3:
    print("{} convertido para HEXADECIMAL é igual a: {}".format(num,hex(num)[2:]))
else:
    print("\033[1;30;41m Opção invalida!! Tente novamente!!\033[m")
