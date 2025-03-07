filmeSet = {"Os increveis", "DeadPool",
"O mascara", "Madagascar", "Os sem Floresta"}

print(type(filmeSet))

#buscando o tamanho do set 
print(len(filmeSet))

# true e um são considerado o mesmo valor
exampleSet = {"Os simpsons", True, 1, 8.6}

print(exampleSet)

# Adiciona item de outro set
filmeSet.update(exampleSet)

print(filmeSet)
# removendo item de um set
filmeSet.remove(True)
filmeSet.remove(8.6)

print(filmeSet)