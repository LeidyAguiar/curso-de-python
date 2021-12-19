string = '012345678901234567890123456789012345678901234567890123456789'
num = 10
lista = [string[i:i + num] for i in range(0, len(string), num)]
retorno = '.'.join(lista)
print(lista)
print(retorno)





