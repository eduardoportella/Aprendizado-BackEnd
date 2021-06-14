from time import sleep
menu = 0
n1 = int(input("Digite o primeiro valor: "))
n2 = int(input("Digite o segundo valor: "))
while menu != 5:
    print("""\n\nMENU
[1] Somar
[2] Multiplicar
[3] Maior
[4] Novos números
[5] Sair do programa""")
    menu = int(input(""))
    if menu == 1:
        print(f'A soma entre {n1} e {n2} é: {n1+n2}')
    elif menu == 2:
        print(f'A multiplicação entre {n1} e {n2} é: {n1*n2}')
    elif menu == 3:
        if n1>n2:
            maior = n1
        else:
            maior = n2
        print(f'O número {maior} é maior')
    elif menu == 4:
        n1 = int(input("Digite o primeiro valor: "))
        n2 = int(input("Digite o segundo valor: "))
    elif menu == 5:
        print("Obrigado por usar :)")
    else:
        print("Opção inválida")
    sleep(2)