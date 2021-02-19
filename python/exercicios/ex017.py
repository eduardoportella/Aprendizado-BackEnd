from math import sqrt
ca = float(input('Digite o tamanho do cateto adjascente: '))
co = float(input('Digite o tamanho do cateto oposto: '))
h = sqrt((pow(ca, 2))+(pow(co, 2)))

print(f'A hipotenusa vale {h:.2f}')