from random import choice
nome1 = input("Digite o primeiro nome: ")
nome2 = input("Digite o segundo nome: ")
nome3 = input("Digite o terceiro nome: ")
arrayDeNomes = [nome1, nome2, nome3]
print(f'O nome escolhido foi {choice(arrayDeNomes)}')
