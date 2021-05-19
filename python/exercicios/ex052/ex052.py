n = int(input("Digite um numero inteiro: "))
contador = 0
for i in range(n, 0, -1):
    if n%i == 0:
        contador = contador + 1
if contador !=2:
    print("Não é primo")
else:
    print("É primo")