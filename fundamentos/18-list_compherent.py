# 1 Listando valores de 0 a 10 que sejam menores de que 4

listNumber = [i for i in range(10) if i < 4 ]
print(listNumber)

# Lista de filme
filmsList = ["Titanic", "Frankestine", "Casa Monstro", "Esquadrão Classe A", "Os Simpsons"]

# filmes que possuem a letra 'C ' No titulo

listFilme = [ filme for filme in filmsList if "c" in filmsList]
print(listFilme)

# filmes que já assiiti

filmesAssist = [filme for filme in filmsList if filme != "Frankestine"]
print(filmesAssist)