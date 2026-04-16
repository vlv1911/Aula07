lst_vazia_meses = [] #Lista vazia
lst_meses = ['Janeiro','Fevereiro','Março','Abril','Maio','Junho']

print(lst_meses[0]) #índice 0 (primeiro elemento)
print(lst_meses[2]) #ínfice 2 (terceiro elemento)
print(lst_meses[-1]) # última posição da lista
print(lst_meses[-2]) # penúltima posição da lista

# Fatiamento
print(lst_meses[:3]) # imprime até o índice (3-1).
print(lst_meses[2:]) # imprime a partir do índice 2 até o final.
print(lst_meses[2:4]) # imprime a partir do índice 2 e vai até o (4-1).


print(lst_meses)

# For em lista

for m in lst_meses:
    print(m)