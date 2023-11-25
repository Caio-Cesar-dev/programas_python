print('-=-'*10)
print("   Analisador de triângulos")
print('-=-'*10)

r1=float(input("Primeiro segmento: "))
r2=float(input("Segundo segmento: "))
r3=float(input("Terceiro segmento: "))
print('-'*30)
if r1 < r2 +r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print("\033[1;34;40m Os segmentos acima PODEM FORMAR triângulo!\033[m")
else:
    print("\033[1;31;40m Os segmentos acima NÃO PODEM FORMAR triângulo!\033[m") # O '\033[m' delimita o preenchimento de fundo