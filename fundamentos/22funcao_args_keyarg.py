"""
args: utilizamos quando não temos certeza de quantos argumentos queremos em uma função 
Os argumentos são pasados como uma tupla
kwargs: Alem dos valores podemos passar tambem as respectivas chaves para cada argumento
Os argumentos são pasado como dicionario
"""

# 1 soma de números
def sum(*num):
    sum_total = 0
    for n in num:
        sum_total += n
    print(f"Soma é: {sum_total}")

sum(7)
sum(7,9)
sum(8, 9, 34, 5, 22)

# 2 - apreswentação de curso    
def apresetacao(**data):
    for key, value in data.items():
        print(f"{key} - {value}")

print("Lista de Cursos")
apresetacao(nome="Python", categoria="Beck-end", level="Iniciante")
apresetacao(nome="Django", categoria="Beck-end", level="iniciante-avançado")