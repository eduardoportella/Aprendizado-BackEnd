valorImovel = float(input('Digite o valor do imóvel: '))
salario = float(input('Digite o salário do cliente: '))
anoEmprestimo = int(input('Em quantos anos? '))
prestacao = valorImovel/anoEmprestimo
print(f'O valor da prestação será de R${prestacao:.2f}')
if (prestacao <= salario*0.3):
    print("Empréstimo autorizado!")
else:
    print("Empréstimo negado!")