l = float(input("Digite aqui a largura da sua parede: "))
a = float(input("Digite aqui a altura da sua parede: "))

area = l*a
qtd = area/2

print("Sua parede tem dimensão {}x{} e sua área é de {}m².\nPara pintar essa parede, você precisará de {:.2f}l de tinta.".format(l, a, area, qtd))

