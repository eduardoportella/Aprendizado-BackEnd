n1 = int(input('Digite um número inteiro: '))
baseConversao = int(input(("""Digite qual será a base de conversão:
1- Binário
2- Octal
3- HexaDecimal\n""")))

if (baseConversao == 1):
    print(bin(n1)[2:])
elif (baseConversao == 2):
    print(oct(n1)[2:])
elif (baseConversao == 3):
    print(hex(n1)[2:])
else:
    print('ERRO')