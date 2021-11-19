"""
* Criar variáveis para nome (str), idade (int), altura (float) e peso (float) de uma pessoa.
* Criar variável com o ano atual (int)
* Obter o ano de nascimento da pessoa (baseado na idade e no ano atual)
* Obter o IMC da pessoa com 2 casas decimais (peso e na altura da pessoa)
* Exibir um texto com todos os valores na tela usando F-Strings (com as chaves)
"""

nome = 'Leidy'
idade = 26  
altura = 1.56 
peso = 56
ano_atual = 2021
nascimento = ano_atual - idade
imc = peso / (altura * altura)

print(f'{nome} tem {idade} anos e {altura} de altura.')
print(f'{nome} pesa {peso} kg e seu IMC é {imc:.2f}.')
print(f'{nome} nasceu em {nascimento}.')