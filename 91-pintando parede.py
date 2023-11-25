alt=float(input("Digite a altura da parede: "))
larg=float(input("Digite a largura da parede: "))

area= larg*alt

print("Sua parede tem a dimensão de {} x {} e a sua area é de {} m²" .format(larg,alt,area))
print("Para pintar essa parede você precisará de %.2f litros de tinta." %(area/2) )