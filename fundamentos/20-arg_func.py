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