import itertools

string = input('Texto a ser permutado: ')

resultado = itertools.permutations(string, len(string))

for i in resultado:
    print(''.join(i))

