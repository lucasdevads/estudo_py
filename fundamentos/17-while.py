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

