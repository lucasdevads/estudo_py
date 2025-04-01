# função de potencia de lambda
power = lambda num:num ** 2 

# verifica se o numero e par
is_even = lambda x: x % 2 == 0

# função que divide um numero por outro
div_num = lambda x, y: x / y

#função que inverte uma striung
reverse = lambda s: s [::-1]

print(power(8))
print(power(9))
print(is_even(23))
print(is_even(66))
print(div_num(10,2))
print(div_num(165,6))
print(reverse("Lucas"))notas = {
    "Meu malvado favorito":[8.0, 9.8,8.0],
    "Os simpsons": [9.0,9.0,9.5],
    "Esquadrão classe A":[8.5, 9.0, 9.5],
     "A casa monstro":[7, 8, 6],
     "Vida de inseto":[7, 8, 8],
     "Como treinar seu dragão":[10, 95, 9]

         }

#funcção para calcular a media de avaliação de um filme


avaliar_filme = lambda nome_filme: sum(notas[nome_filme])/ len(notas[nome_filme])

# função que verifica se o filme está na lista

check_filme = lambda nome_filme: nome_filme in filme_list

# função para recomendar filme com base na avaliação media

recomenda_filme = lambda nome_filme: f"Recomendo assitir {nome_filme} com média de {notas(nome_filme):.2f}"


print(f"A média de avaliação do filme Como treinar seu dragão: {avaliar_filme("Como treinar seu dragão")}")
print(f"Vida de inseto está na lista? {check_filme("Vida de inseto")}")
print(f"{recomenda_filme("Os simpsons")}")