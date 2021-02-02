dias = int(input('Quantos dias você ficou com o carro? '))
km = float(input('Quantos Km foram rodados? '))
tot = (dias*60) + (km*0.15)
print(f'O total a pagar é R${tot:.2f}')