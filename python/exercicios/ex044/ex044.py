preco = float(input('Digite o preco das compras: R$'))
print("""Como será a forma de pagamento?
[1] à vista (dinheiro/cheque)
[2] à vista cartão
[3] 2x no cartão
[4] 3x ou mais no cartão""")
opcao = int(input(''))
if opcao == 1:
    preco = preco- preco*0.1
elif opcao == 2:
    preco = preco - preco*0.05
elif opcao == 3:
    preco = preco #colocando aq pra nao cair no else
elif opcao == 4:
    preco = preco + preco*0.2
else:
    print("ERRO")

if opcao >=1 and opcao <= 4:
    print(f'O preco total será de R${preco:.2f}')