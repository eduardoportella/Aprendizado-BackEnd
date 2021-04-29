from datetime import datetime
ano = datetime.now().year
anoNasc = int(input('Digite o ano de nascimento do atleta: '))
idade = ano-anoNasc
if (idade<=9):
    print('Atleta Mirim')
elif (idade <= 14):
    print('Atleta Infantil')
elif (idade <= 19):
    print('Atleta Júnior')
elif (idade <= 25):
    print('Atleta Sênior')
else:
    print('Atleta Master')