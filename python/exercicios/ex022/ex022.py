nome = str(input("digite seu nome completo: ")).strip()
print(f'Seu nome em maiúsculas é "{nome.upper()}"')
print(f'Seu nome em minúsculas é "{nome.lower()}"')
print(f'Seu nome ao todo tem {len(nome) - nome.count(" ")} letras')
separa = nome.split() #LEMBRAR Q SPLIT() TRANSFORMA EM VETOR
print(f'Seu primeiro nome é "{separa[0]}" e ele tem {len(separa[0])} letras')