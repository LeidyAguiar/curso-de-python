"""
CPF = 168.995.350-09
------------------------------------------------
1 * 10 = 10           #    1 * 11 = 11 <-
6 * 9  = 54           #    6 * 10 = 60
8 * 8  = 64           #    8 *  9 = 72
9 * 7  = 63           #    9 *  8 = 72
9 * 6  = 54           #    9 *  7 = 63
5 * 5  = 25           #    5 *  6 = 30
3 * 4  = 12           #    3 *  5 = 15
5 * 3  = 15           #    5 *  4 = 20
0 * 2  = 0            #    0 *  3 = 0
                      # -> 0 *  2 = 0
         297          #             343
11 - (297 % 11) = 11  #     11 - (343 % 11) = 9
11 > 9 = 0            #
Digito 1 = 0          #   Digito 2 = 9
"""

cpf_str = input('Digite seu CPF: ')
cpf_str = cpf_str.replace('.', '').replace('-', '')
cpf_gerado = cpf_str[:-2] # Elimina os dois últimos digitos do CPF

if not cpf_str.isnumeric():
    print('Isso não é um número.')
else:
    soma = 0
    for i, regressivo in enumerate(range(10, 1, -1)):
        multiplicar = int(cpf_gerado[i]) * regressivo
        # print(f'{cpf_gerado[i]} * {regressivo} = {multiplicar}')
        soma = soma + multiplicar
    digito_1 = 11 - (soma % 11)

    if digito_1 > 9: # Se o digito for > que 9 o valor é 0
        digito_1 = 0
    cpf_gerado += str(digito_1)

    soma = 0
    for i, regressivo in enumerate(range(11, 1, -1)):
        multiplicar = int(cpf_gerado[i]) * regressivo
        # print(f'{cpf_gerado[i]} * {regressivo} = {multiplicar}')
        soma = soma + multiplicar
    digito_2 = 11 - (soma % 11)

    if digito_2 > 9: 
        digito_2 = 0
    cpf_gerado += str(digito_2) # Concatena o digito gerado no novo cpf

    # Evita sequencias. Ex.: 11111111111, 00000000000...
    sequencia = cpf_gerado == str(cpf_gerado[0]) * len(cpf_str)
    if cpf_str == cpf_gerado and not sequencia:
        print('CPF Válido')
    else:
        print('CPF Inválido')