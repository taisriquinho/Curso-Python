# Informações sobre o filme
name = input("Digite o nome do filme:\n")
ano = int(input("Digite o ano de lançamento: \n"))
nota = float(input("Digite a nota de avaliação do filme:\n"))

# Verifica se o filme é recomendado
if nota > 8.0 and ano > 2015:
    print(f"O filme {name} é muito bom. Recomendo assistir")
else:
    print(f"O filme {name} ainda não atingiu uma boa nota")

num1 = float(input("Digite um numero: "))
num2 = float(input("Digite outro numero: "))
operacao = input("Digite a operação a ser realizada (+ - * /): ")

if operacao == "+":
    resultado = num1+num2
elif operacao == "-":
    resultado = num1-num2
elif operacao == "*":
    resultado = num1*num2
elif operacao == '/':
    if num2 != 0:
        resultado = num1/num2
    else:
        print("Erro")
else:
    print("Operação inválida")
    resultado = 0

print(f"Resultado da operação é: {resultado:.2f}")
