import random
itens = ('Pedra', 'Papel', 'Tesoura')
computador = random.randint(0, 2)
print("""[0] PEDRA
[1] PAPEL
[2] TESOURA""")
resp = int(input("Qual é sua jogada? "))
print(f'Computador jogou {itens[computador]}')
if resp>=0 and resp<=2:
    print(f'Jogador jogou {itens[resp]}')
if computador == 0:
    if resp == 0:
        print("Empatou!")
    elif resp == 1:
        print("Você ganhou!")
    elif resp == 2:
        print("Você perdeu!")
    else:
        print("Jogada inválida")
elif computador == 1:
    if resp == 0:
        print("Você perdeu!")
    elif resp == 1:
        print("Empatou!")
    elif resp == 2:
        print("Você ganhou!")
    else:
        print("Jogada inválida")
else:
    if resp == 0:
        print("Você ganhou!")
    elif resp == 1:
        print("Você perdeu!")
    elif resp == 2:
        print("EMPATOU!")
    else:
        print("Jogada inválida")