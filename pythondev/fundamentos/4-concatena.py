name = input("Digite o nome do filme: \n")
yearLauch = int(input("Digite o ano de lançamento do filme: \n"))
noteMovie = float(input("Digite a nota do filme: \n"))
print("Dados do Filme")
print("======================================")

# Alternativa 1
print("Nome do Filme: ", name)
print("Ano do filme: ", yearLauch)
print("Nota do Filme: ", noteMovie )

# Alternativa 2
print("Nome do filme", name, "\nAno do Filme", yearLauch, "\nNota do Filme: ", noteMovie)

# Alternativa 3
print(f"Nome do filme:: {name}\n"
      f"Ano de Lançamento: {yearLauch}\n"
      f"Nota do Filme: {noteMovie}\n"
      )