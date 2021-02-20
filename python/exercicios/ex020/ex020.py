import random
nome1 = input("Digite o primeiro aluno: ")
nome2 = input("Digite o segundo aluno: ")
nome3 = input("Digite o terceiro aluno: ")
nome4 = input("Digite o quarto aluno: ")
arrayDeNomes = [nome1, nome2, nome3, nome4]
random.shuffle(arrayDeNomes)

print(f'A ordem será: {arrayDeNomes}')
