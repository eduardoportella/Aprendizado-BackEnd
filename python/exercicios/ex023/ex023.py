num = int(input("Digite um numero de 0 a 9999:"))
print(f'Unidade: {num//1%10} \nDezena: {num//10%10} \nCentena: {num//100%10}\nMilhar: {num//1000%10}')