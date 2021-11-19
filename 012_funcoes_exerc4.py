"""
4 - Fizz Buzz - Se o parâmetro da função for divisível por 3, retorne fizz,
se o parâmetro da função for divisível por 5, retorne buzz. Se o parâmetro da
função for divisível por 5 e por 3, retorne FizzBuzz, caso contrário, retorne o
número enviado.
"""

def fb(num):
    if num % 3 == 0 and num % 5 == 0:
        return f'FizzBuz, {num} é divisível por 3 e 5'
    if num % 5 == 0:
        return f'buzz, {num} é divisível por 5'
    if num % 3 == 0:
        return f'fizz, {num} é divisível por 3'
    return num


from random import randint

for i in range(100):
    aleatorio = randint(0, 100)
    print(fb(aleatorio))
