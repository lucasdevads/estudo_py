# # informações sobre o filme
# nome = input("Digite o nome do Filme: \n")
# anoFilme = int(input("Digite o ano de lançamento: \n"))
# avaliação = float(input("Digite a nota de avaliação do Filme: \n")) 

# #verificar se o filme e recoemndado

# if avaliação > 8.0 and anoFilme > 2015:
#     print(f"O filme {nome} é muito bom. Recomendo assisti-lo")
# else:
#     print(f"O filme {nome} ainda não atingiu uma boa nota!")


num1 = float(input("Digite o primeiro numero: \n"))
num2 = float(input("Digite o segundo numero: \n"))
operacao = input("Digite a operação a ser realizada: (+ , - , * , /) ")

if operacao == "+":
    result = num1 + num2
elif operacao == "-":
    result = num1 - num2
elif operacao == "*":
    result = num1 * num2
elif operacao == "/":
    if num2 != 0:
        result = num1 / num2
    else:
        print("Error, Divisão por Zero")
        result = 0
else:
    print("Operação invalida")
    result = 0

print(f"Resltado da operação é : {result:.2f}")

