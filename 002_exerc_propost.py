"""
- Faça um programa que peça ao usuário para digitar um número inteiro, informe se este número é par ou ímpar. Caso o usuário não digite um número inteiro, 
  informe que não é um número inteiro.
"""

numero_inteiro = input('Digite um número inteiro: ')

if not numero_inteiro.isdigit():
    print('Isso não é um número inteiro')
else:
    numero_inteiro = int(numero_inteiro)

    if not numero_inteiro % 2 == 0:
        print(f'{numero_inteiro} é ímpar')
    else:
        print(f'{numero_inteiro} é par')