listafilmes = ["Flow", "10 coisas que odeia em você", "Jogo da imitação",
               "It: a coisa", "Superman"]

#tamanho da lista
print(len(listafilmes))

#recuperar item da lista pelo nome
print(listafilmes.index("Superman"))

#adicionar um item ao final da lista
listafilmes.append('The Others')
print(listafilmes)

#ordenar a lista
listafilmes.sort()
print(listafilmes)

#copiar os itens de uma lista para outra
copiaLista = listafilmes.copy()
copiaLista.remove('Superman')
print(copiaLista)

#remove todos os itens da lista
listafilmes.clear()
print(listafilmes)
