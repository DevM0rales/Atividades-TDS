"""
Formatação básica de Strings
s - strings 
d - int 
f - float 
x - Hexadecimal

"""

variavel = 'ABC'
print(f'{variavel}')
print(f'{variavel: >10}.')
print(f'{variavel: <10}')
print(f'{variavel: ^10}')

try:
    pinto = int(input("fodase: "))
except ValueError:
    print("tu é um cu preto")