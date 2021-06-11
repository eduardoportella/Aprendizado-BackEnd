for i in range(1,6):
    peso = int(input(f'Digite o peso da pessoa {i}: '))
    if (i==1):
        menorPeso = peso
        maiorPeso = peso
    if (peso>maiorPeso):
        maiorPeso = peso
    if (peso<menorPeso):
        menorPeso = peso
print(f'O maior peso foi de {maiorPeso} e o menor peso foi de {menorPeso}')
