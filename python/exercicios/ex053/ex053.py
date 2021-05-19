frase = str(input("Digite a frase: "))
frase = frase.replace(" ", "")
fraseInvertida = frase[::-1]
print(frase)
print(fraseInvertida)
if frase == fraseInvertida:
    print("É um palíndromo")
else:
    print("Não é um palíndromo")