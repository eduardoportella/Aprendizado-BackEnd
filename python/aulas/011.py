print("\033[1;31;43m")
print("Olá mundo")

print("\033[30;42mEduardo\033[m")
print("Portella")
print("\033[7m Negativo \033[m")

print(f'A soma entre \033[31m{3}\033[m e \033[32m{5}\033[m é \033[33m{3+5}\033[m')

nome = 'Edu'
cores = {
    'limpa' : '\033[m',
    'azul' : '\033[34m',
    'amarelo' : '\033[33m',
    'pretoebranco' : '\033[7;30m' 
}

# print(f'Olá, muito prazer, {cores['amarelo']}{nome}{cores['limpa']}')
print('Olá, muito prazer, {} {} {}'.format(cores['amarelo'], nome, cores['limpa']))