nomefilme = "Esquadrão classe A"

#string[inicio:fim] começa na posição zero | indice final -1
# 1 Buscar  toda a string apartir da primeira posição
print(nomefilme[0:])

# 2 buscar a string até a ultima posição

print(nomefilme[:17])

# 3 buscar apartir da 3º posição
print(nomefilme[3:])

"""
string[inicio:fim] começa na posição zero | indice final -1
passo - determina o incremento. Por padrão e 1

"""
# 4 buscando a string de 2 em 2
print(nomefilme[::2])

# 5 buscando a string nos numeros impas
print(nomefilme[1::2])

# 6 invertendo uma string
print(nomefilme[::-1])