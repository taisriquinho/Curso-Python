movieName = 'Flow'
movieDescription = """
    Flow é um filme de animação de 2024, que conta a história de um gato, 
onde seu lar é devastado por uma inundação
"""
print(movieName.upper()) #tudo maiúsculo
print(movieName.lower()) #tudo minúsculo
print(movieName.capitalize()) #primeira letra em maiúsculo
print(movieName.title()) #primeira letra em maiúsculo
print(movieName.center(10, '-')) #retorna string centralizada com caractere de preenchimento
print(movieName.find('o')) #retorna posição/indice do caractere
print(movieName.replace("Flow", "Filme do gato")) #altera elemento por outro
print(movieDescription.split(',')) #quebra linha quando encontra caractere
