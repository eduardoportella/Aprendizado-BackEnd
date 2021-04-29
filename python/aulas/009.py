frase = 'Eduardo Francisco Ribas Portella'
print(frase[1])
print(frase[10:])
print(frase[:13])
print(frase[1:15])
print(frase[1:15:2])
print(frase[::2])
print(len(frase))
print(frase.count('o'))
print(frase.upper().count('E'))
dividido = frase.split()
print(dividido[2][3])

frase2 = '      Nao'
print(frase2)
frase2 = frase2.split()
print(frase2)
# print(frase2.lower().find('nao'))

print('\n')

print("""B
o
m

d
i
a!""")