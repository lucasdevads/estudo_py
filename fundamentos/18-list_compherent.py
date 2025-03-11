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

# encontrando um filme pelo nome

while True:
    buscaNome = input("Digite o nome do filme para buscar na lista ( ou sair para encerrar) \n")
    if buscaNome.lower() == "sair":
        print("Programa Encerrado")
        break
    encontraFilme = [ filme for filme in filmsList if buscaNome.lower() in filme.lower()]
    if encontraFilme:
        print(f"filme(s) encontrado(s) com o nome : {buscaNome}:")
        for encontrar in encontraFilme:
            print(encontrar)
        else:
            print(f"Nenhum filme foi encontrado com o nome {buscaNome}")

        