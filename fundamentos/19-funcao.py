# função para imprimir uma mensagem 
def bemVindo():
    print("Bem Vindo ao Sistema de Filmes")

# for i in range(10):
#     bemVindo()

# função para calcular media de notas

def calculete():
    contidade = int(input("Digite quantas avaliações deseja fazer: \n"))
    total = 0
    for i in range(contidade):
        nota = float(input("Digite a nota para o filme: \n"))
        total += nota

    if contidade > 0:
        media = total / nota
    else:
        media = 0
    return media

print(f"A média de avalições: {calculete():.2f}")