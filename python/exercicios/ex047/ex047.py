pares = 0
for cont in range(1, 51):
    if (cont%2 == 0):
        print(cont, end=' ')
        pares = pares + 1
print(f'\nExistem {pares} pares no intervalo')