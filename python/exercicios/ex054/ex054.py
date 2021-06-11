from datetime import date
data = date.today().year
totMaior = 0
totMenor = 0
for i in range(1, 8):
    idade = int(input(f'Digite o ano de nascimento pessoa número {i}: '))
    idade = data-idade
    if (idade >= 18):
        totMaior = totMaior+1
    else:
        totMenor = totMenor+1
print(f'Foram citadas {totMaior} pessoas maiores de idade e {totMenor} pessoas menores de idade')
