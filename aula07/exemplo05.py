# título, autor, ano de publicação, gênero, e número de páginas:

livros = []
for l in range(2):
    print(f'\nLivro {l+1}')

    livro = {}
    livro['titulo'] = input('Nome do livro: ')
    livro['autor'] = input('Nome do autor: ')
    livro['ano'] = int(input('Ano de publicação: '))
    livro['genero'] = input('Gênero do livro: ')
    livro['titulo'] = int(input('Número de páginas: '))

    livros.append(livro)
    print('Livro cadastrado')

# mostrando:
    
print('\n -- Livros a partir de 2010 --')
for l in livros:
    if l['ano'] >= 2010:
        print(l)
