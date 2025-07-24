filmeFlow = {
    "titulo": "Flow",
    "ano": 2025,
    "nota": 8.8,
    "genero": ["Animação", "Drama"]
}

print(filmeFlow)
print(len(filmeFlow))
print(type(filmeFlow))

#Recuperar elemento do dicionario
print(filmeFlow["genero"])
print(filmeFlow.get("nota"))

#Buscar apenas as chaves do dicionario
print(filmeFlow.keys())

#Buscar apenas os valores do dicionario
print(filmeFlow.values())

#Buscar itens do dicionario com a chave e valor
print(filmeFlow.items())

#Adicionar itens no dicionario
filmeFlow["Oscar"] = 'Sim'
print(filmeFlow)

#Atualizar itens dicionario
filmeFlow.update({"nota": 8.7})
print(filmeFlow)

#Remover item dicionario
filmeFlow.pop("Oscar")
print(filmeFlow)


