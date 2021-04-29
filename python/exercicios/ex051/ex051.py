print("10 termos de uma P.A.")
primeiroTermo = int(input("Primeiro termo: "))
razao = int(input("Razão: "))
for cont in range(0, 10):
    print(primeiroTermo, end=' -> ')
    primeiroTermo = primeiroTermo + razao
print("ACABOU")