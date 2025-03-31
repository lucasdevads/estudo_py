"""
args: utilizamos quando não temos certeza de quantos argumentos queremos em uma função 
Os argumentos são pasados como uma tupla
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