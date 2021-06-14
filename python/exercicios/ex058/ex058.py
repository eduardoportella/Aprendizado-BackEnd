from random import randint
n = randint(1, 10)
resp = int(input("Digite sua resposta: "))
palpites = 1
while resp != n:
    resp = int(input("Você errou. Tente novamente: "))
    palpites += 1
print(f'Parabéns você acertou usando {palpites} palpites')
