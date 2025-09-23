# nome = 'Lucas'

# print('cas' in nome)
# print('L' in nome)
# print('cas' not in nome)
# print('L' not in nome)


nome = input('Digite seu nome: ')
procurar = input("Oque você deseja procurar: ")

if procurar in nome:
    print(f'{procurar} está em nome')
else:
    print(f"{procurar} não está em {nome}")
    