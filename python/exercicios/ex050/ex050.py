soma = 0
for cont in range(1, 7):
    n = int(input(f'Digite o {cont}º numero: '))
    if (n%2==0):
        soma = soma + n
print(f'A soma dos números pares é de: {soma}')