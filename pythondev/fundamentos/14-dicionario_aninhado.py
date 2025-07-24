import pprint

dicionarioFilmes = {
    "Flow":{
        "ano": 2025,
        "nota": 8.8,
        "genero": ["Animação", "Drama"]
    },
    "Superman":{
        "ano": 2025,
        "nota": 8.5,
        "genero": ["Ação", "Sci-fi"]
    }
}

pp = pprint.PrettyPrinter(depth = 4)
pp.pprint(dicionarioFilmes)

#Buscar uma informação dentro de um dicionario aninhado
print(dicionarioFilmes["Flow"]["genero"])

#Adicionar novo item
dicionarioFilmes["Flow"]["Oscar"] = "Sim"
print(dicionarioFilmes["Flow"])

#Excluir um dicionario
del dicionarioFilmes["Flow"]
pp.pprint(dicionarioFilmes)