filmsList = ["Titanic", "Frankestine", "Casa Monstro", "Esquadrão Classe A", "Os Simpsons"]
# numros = [12, 34,45, 5, 56, 67, 34, 90, 45, 34, 65, 87,100]
# 1 interando valores de uma lista
# for numero in numros:
#     print(numero)


for filme in filmsList:
    print(filme)

# quando a condição for atendida o loop sera encerrado

for filme in filmsList:
    if filme == "Casa Monstro":
        break
    print(filme)

# quando a condição for atendida o loop vai para a proximo iteração

for filme in filmsList:
    if filme == "Casa Monstro":
        continue
    print(filme)

# 4 avaliçaõ do filme
nomeFilme = input("Digite o nome do Filme: \n")
avaliacaoFilme = int(input("Digita quantas avaliações deseja fazer:\n"))

total = 0

for i in range(avaliacaoFilme):
    note = float(input("Digite a nota do filme: \n"))
    total += note

if avaliacaoFilme > 0:
    media = total / avaliacaoFilme
else:
    media = 0

print(f"Média de avaliação do filme {nomeFilme} é: {media:.2f}")