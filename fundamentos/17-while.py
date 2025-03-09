filmsList = ["Titanic", "Frankestine", "Casa Monstro", "Esquadrão Classe A", "Os Simpsons"]

# iteradno valores de uma lista com while

index = 0 
while index < len(filmsList):
    print(filmsList[index])
    index += 1

# quando a condição for atendida vai ser encerado loop

index = 0 
while index < len(filmsList):
    if filmsList[index] == "Casa Monstro":
        break
    print(filmsList[index])
    index += 1


#  Quando a condição for atendida o loop vai para a proxima iteração

index = 0 
while index < len(filmsList):
    if filmsList[index] == "Casa Monstro":
        index += 1
        continue
    print(filmsList[index])
    index += 1

# avaliação com while 

nomeFilme = input("Digite o nome do Filme: \n")
avaliacaoFilme = int(input("Digita quantas avaliações deseja fazer:\n"))

total = 0
contar = 0

while contar < avaliacaoFilme:
    note = float(input("Digite a nota para o filme: \n"))
    total += note
    contar += 1

if avaliacaoFilme > 0:
    media = total / avaliacaoFilme
else:
    media = 0

print(f"Média de avaliação do filme {nomeFilme} é: {media:.2f}")