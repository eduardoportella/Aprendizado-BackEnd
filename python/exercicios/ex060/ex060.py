n = int(input("Digite um número para calcularmos seu fatorial: "))
aux = n
fatorial = 1
while n>1:
    fatorial *=n
    n -= 1
print(f'O fatorial de {aux} é de {fatorial}')