frase = str(input("Digite uma frase: ")).lower()
# contadorDeLetraA = frase.count('a')
# primeiraPosicaoA = frase.find('a')+1
# ultimaPosicaoA = frase.rfind('a')+1
# print(f'A letra A aparece {contadorDeLetraA} vezes na frase')
# print(f'A primeira letra A apareceu na posição {primeiraPosicaoA}')
# print(f'A última letra A apareceu na posição {ultimaPosicaoA}')
# Sem variavel nao funciona o f'

print('A letra A aparece {} vezes na frase'.format(frase.count('a')))
print('A primeira letra A apareceu na posição {}'.format(frase.find('a')+1))
print('A última letra A apareceu na posição {}'.format(frase.rfind('a')+1))