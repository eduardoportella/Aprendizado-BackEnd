soma = 0
for cont in range(1, 501, 2): ##como o exercicio eh so para os numeros impares, o for pula os pares
    if (cont%3 == 0):
        soma = soma + cont
print(f'A soma dos múltiplos de 3 de 1 até 500 é de: {soma}')