"""Exercício Python 094: Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada
pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre: A) Quantas pessoas foram cadastradas
B) A média de idade C) Uma lista com as mulheres D) Uma lista de pessoas com idade acima da média"""
cadastro=[]
persona={}
soma_idade=0
while True:
    persona['nome']=str(input('Nome: '))
    while True:
        persona['sexo']=str(input("Sexo [M/F]: ")).upper()[0]
        if persona['sexo'] in 'MF':
            break
        print('ERRO! Por favor, digite apenas M ou F! ')
    persona['idade']=int(input("Idade: "))
    soma_idade+=persona['idade']
    cadastro.append(persona.copy())
    persona.clear()
    s_n=int(input("Deseja continuar? (0 para Sair!)"))
    if s_n == 0:
        print("*********=====SAIR====*********")
        print()
        break
print(f"Foi cadstrado um total de {len(cadastro)} pessoas.")
print(f"A média de idade foi: {soma_idade/len(cadastro):5.2f} anos.")
print(f'As mulheres cadastradas foram: ',end='')
for p in cadastro:
    if p['sexo'] in 'Ff':
        print(f'{p["nome"]} ',end='')
print()
print(f'As pessoas com mais de 18 foram: ',end='')
media=(soma_idade/len(cadastro))
for p in cadastro:
    if p['idade'] >=media:
        print(f'{p["nome"]} ',end='')
        print('    ')
        for k, v in p.items():
            print(f'{k}  =  {v}; ',end='')
        print()
print('<< ENCERRRADO >>')



