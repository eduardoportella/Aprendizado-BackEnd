somaIdade = 0
mulheresMenos20Anos = 0
homemVelho = 0
for i in range(1,5):
    idade = int(input(f'Digite a idade da pessoa {i}: '))
    somaIdade = somaIdade + idade
    sexo = str(input(f'Digite o sexo da pessoa {i} [mas/fem]: '))
    if (idade < 20 and sexo=='fem'):
        mulheresMenos20Anos += 1
    if (homemVelho<idade and sexo=='mas'):
        homemVelho = idade
media = somaIdade/4
print(f'\nO homem mais velho tem {homemVelho} anos')
print(f'A média de idade do grupo é de {media}')
print(f'Existem {mulheresMenos20Anos} mulheres com menos de 20 anos')