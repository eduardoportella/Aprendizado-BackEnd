import random
from time import sleep
aleatorio = random.randint(0,5)
print('-'*50)
print("Vou pensar em um número de 0 a 5, adivinhe")
print('-'*50)
n = int(input("Em que número eu pensei? "))
print("PROCESSANDO...")
sleep(3)
if aleatorio == n:
    print("Você acertou!")
else:
    print(f'Você errou, meu número era {aleatorio}')