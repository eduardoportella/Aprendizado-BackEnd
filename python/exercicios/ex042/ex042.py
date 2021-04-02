n1 = float(input('Digite o tamanho do primeiro lado: '))
n2 = float(input('Digite o tamanho do segundo lado: '))
n3 = float(input('Digite o tamanho do terceiro lado: '))
if n1==n2 and n1 == n3:
    print('O triâgunlo é equilátero')
elif (n1==n2 and n1 != n3) or (n2==n3 and n2 != n1) or (n1==n3 and n1!=n2):
    print('O triâgunlo é isósceles')
else:
    print('O triângulo é escaleno')
