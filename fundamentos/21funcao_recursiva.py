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
