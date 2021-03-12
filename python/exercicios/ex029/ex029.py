vel = float(input("Digite a velocidade atual do carro: "))
limite = 80
if vel >limite:
    print(f'Você excedeu o limite de {limite}km/h \nVocê deve pagar uma multa de R$280,00!')
else:
    print("Tenha um bom dia! Dirija com segurança!")