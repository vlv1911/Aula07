list_produtos = ['Notebook','Mouse','Teclado','Monitor']

list_produtos[0] = 'PC'
print(f'Altera o primeiro elemento {list_produtos}')

list_produtos.append('Webcam')
print(f'Produto adicionado {list_produtos}')

list_produtos.remove('Monitor')
print(f'Produto removido {list_produtos}')

list_produtos.pop() #remove o úlimo ítem da lista
print(f'Produto o último {list_produtos}')

del list_produtos[0]
print(f'Produto removido por posição {list_produtos}')
