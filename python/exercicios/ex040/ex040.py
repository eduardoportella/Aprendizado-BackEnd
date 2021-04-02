nota1 = float(input("Digite a primeira nota do aluno: "))
nota2 = float(input("Digie a segunda nota do aluno: "))
media = (nota1+nota2)/2
print(f'A média do aluno é: {media:.2f}')
if media <5:
    print('Reprovado')
elif media>=5 and media<7:
    print('Recuperação')
else:
    print('Aprovado')