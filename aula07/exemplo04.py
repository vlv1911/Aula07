# Dicionários:

pessoa_vazio = {}

pessoa= {}
pessoa['Nome'] = 'João'
pessoa['Idade'] = 25
pessoa['Cidade'] = 'Níterói'
print(pessoa)

# Acessando e mostrando o valor de uma chave:
print(pessoa['Cidade'])

# Alterando o valro da chave:
pessoa['Idade'] = 26
print(pessoa)

# Adicionando uma nova chave
pessoa['Profissao'] = 'Programador'
print(pessoa)

# Deletando uma chave:

del pessoa['Cidade']
print(pessoa)

