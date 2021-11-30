print('Sistema de perguntas e respostas com dicionários em Python')

"""
# Exemplo
Pergunta 1: Quanto é 1 + 1?
Respostas:
[a]: 2
[b]: 4
[c]: 5
Sua resposta: a
"""

perguntas = {
    'Pergunta 1': {
        'pergunta': 'Quanto é 2 + 2? ',
        'respostas': {
            'a': '2',
            'b': '4',
            'c': '5',
        },
        'resposta_certa': 'b',
    },
    'Pergunta 2': {
        'pergunta': 'Quanto é 3x2? ',
        'respostas': {
            'a': '4',
            'b': '101',
            'c': '6',
        },
        'resposta_certa': 'c'
    },
    'Pergunta 3': {
        'pergunta': 'Quanto é 10+10? ',
        'respostas': {
            'a': '10',
            'b': '20',
            'c': '40',
        },
        'resposta_certa': 'b',
    },
    'Pergunta 4': {
        'pergunta': 'Quanto é 8/4? ',
        'respostas': {
            'a': '3',
            'b': '4',
            'c': '2',
        },
        'resposta_certa': 'c',
    },
    'Pergunta 5': {
        'pergunta': 'Quanto é 10*10? ',
        'respostas': {
            'a': '100',
            'b': '200',
            'c': '10',
        },
        'resposta_certa': 'a',
    },
}
print()

respostas_certas = 0
for pergunta, dados_pergunta in perguntas.items():
    print(f'{pergunta}: {dados_pergunta["pergunta"]}')
    print('Respostas: ')
    for resposta, dados_resposta in dados_pergunta['respostas'].items():
        print(f'[{resposta}]: {dados_resposta}')

    resposta_usuario = input('Sua resposta: ')

    if resposta_usuario == dados_pergunta['resposta_certa']:
        print('Ebaaaaaaa!!! Você acertou!!!')
        respostas_certas += 1
    else:
        print('Que pena!!! Você errou!!!')
    print()
qtd_perguntas = len(perguntas)
porcentagem_acerto = respostas_certas / qtd_perguntas * 100
print(f'Você acertou {respostas_certas} resposta(s).')
print(f'Sua porcentagem de acerto foi {porcentagem_acerto}%.')