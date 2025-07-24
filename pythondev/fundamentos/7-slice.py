movieName = '10 coisas que odeio em você'
# String[inicio:fim] - índice começa da posição 0 | índice final -1

# 1 - Buscar toda string a partir da primeira posição
print(movieName[0:])

# 2 - Buscar toda string até a última parte
print(movieName[:27])

# 3 - Buscar toda string a partir da terceira até a última posição
print(movieName[2:])

"""
String[inicio:fim:passo] 
índice começa da posição 0 | índice final -1
passo - determina incremento. Por padrão passo = 1
"""
# 4 - Buscar string de 2 em 2 caracteres
print(movieName[::2])

# 5 - Buscar toda string nos índices impares
print(movieName[1::2])

# 6 - Inverter uma string de trás para frente
print(movieName[::-1])