filmesSet = {"Flow", "10 coisas que odeia em você", "Jogo da imitação",
               "It: a coisa", "Superman"}

print(type(filmesSet))

#Buscar tamanho do set
print(len(filmesSet))

#Adicionar item de outro set
exampleSet = {"Flow", True, 1, 8.7}
filmesSet.update(exampleSet)
print(filmesSet)

#Remover um item no set
filmesSet.remove(True)
print(filmesSet)