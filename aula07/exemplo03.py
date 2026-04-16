
# V0 = float(input('Informe o valor da venda: '))
# V1 = float(input('Informe o valor da venda: '))
# V2 = float(input('Informe o valor da venda: '))
# V3 = float(input('Informe o valor da venda: '))
# V4 = float(input('Informe o valor da venda: '))
# V5 = float(input('Informe o valor da venda: '))
# V6 = float(input('Informe o valor da venda: '))
# V7 = float(input('Informe o valor da venda: '))
# V8 = float(input('Informe o valor da venda: '))
# V9 = float(input('Informe o valor da venda: '))

lst_vendas = []

for v in range(10):
    valor_venda = float(input('Informe o valor da venda: '))
    lst_vendas.append(valor_venda)

print(f'As vendas registradas foram: {lst_vendas}')

META = 1000 # Constante (deve ser escrito com letras maiúsculas para diferenciar de variáveis)
META_MINIMA = 700 # Constante (deve ser escrito com letras maiúsculas para diferenciar de variáveis)

for v in lst_vendas:
    if v >= META:
        print(f'Venda de R$ {v}: Meta atingida')
    elif v >= META_MINIMA:
        print(f'Venda de R$ {v}: Mínima atingida')
    else:
        print(f'Venda de R$ {v}: Não atingiu a meta')

print('Programa encerrado.')


