from datetime import datetime
anoNasc = int(input('Digite seu ano de nascimento: '))
anoAgora = datetime.now().year
if anoAgora-anoNasc > 18:
    print(f'Já passou da hora de se alistar, você deveria ter se alistardo à {(anoAgora-anoNasc)-18} ano(s)')
elif anoAgora-anoNasc == 18:
    print("Você tem que se alistar")
else :
    print(f'Ainda faltam {18-(anoAgora-anoNasc)} ano(s) para você se alistar')
