
print("#"*50)
print("Ex 1")
print("#"*50)

nome1 = input("Digite um nome: ")
nome2 = input("Digite outro nome: ")

print(nome1, " ", nome2)

nome = input("Digite seu nome: ")
sobrenome = input("Digite seu sobrenome: ")

nomeFormatado = f"{sobrenome}{nome}"
print(nomeFormatado)

print("#"*50)

print("Ex 2")
print("#"*50)

texto = "Python é muito interessante"
palavras = texto.split()
textoinvertido = " ".join(palavras[::-1])
print(textoinvertido)

print("#"*50)
print("Ex 3")
print("#"*50)

texto1 = "arara"
texto2 = "python"

#kremove espaço em branco
texto1_format = texto1.replace(" ", "")
texto2_format = texto2.replace(" ", "")

palindromo1 = texto1_format == texto1[::-1]
palindromo2 = texto2_format == texto2[::-1]

print(palindromo1)
print(palindromo2)



