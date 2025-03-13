# imprime o nome completo
def nomeCompleto(nome, sobrenome):
    print(f"Nome é: {nome} {sobrenome}")

nomeCompleto("Lucas", "Morais")
nomeCompleto("Joaõ", "Pedro")

# função para somar dois numeros
def soma(a, b):
    return a + b

print(f"A some é: {soma(4, 6)}")


# funcção com paraanmetro default

def enderoco(pais="Brasil"):
    print(f"Eu moro em: {pais}")

enderoco("Irlanda")

# função para avaliar o filme

def avaliarFilme(avaliacaoFilme, nomeFilme):

    total = 0
    for i in range(avaliacaoFilme):
        nota = float(input("Digite a nota para o Filme: \n"))
        total += nota


    if avaliacaoFilme > 0:
        media = total / avaliacaoFilme
    else:
        media = 0

    print(f"Média de avaliação do filme: {nomeFilme} é: {media}")

avaliarFilme(2, "Mario")