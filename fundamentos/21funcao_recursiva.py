"""
fatorial de um numero
1 -> 1 * 1
2 -> 2 * 1
3 -> 3 * 2 * 1
    
"""

# fatorial de um numero

def fatorial(num):
    if num == 1:
        return 1
    return (num * fatorial(num - 1))

number = int(input("Digite o número para o fatorial: \n"))
print(f"O fatorial  de {number} é {fatorial(number)}")

# soma total de um número

def total_sum(num):
    if num == 1:
        return 1
    else:
        return(num + total_sum(num - 1))

num = int(input("Digite o número para a soma: \n"))
print(f"O soma total  de {num} é {total_sum(num)}")