peso = float(input("Digite o seu peso em kg: "))
altura = float(input("Digite a sua altura em metros: "))
IMC = peso/(altura*altura)
if IMC < 18.5:
    print("Abaixo do peso")
elif IMC >= 18.5 and IMC <25:
    print("Peso ideal")
elif IMC >=25 and IMC < 30:
    print("Sobrepeso")
elif IMC >=30 and IMC < 40:
    print("Obesidade")
else:
    print("Obesidade mórbida")
