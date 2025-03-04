
filmeList = ["Os simpsons", "DeadPool",
"O mascara", "Madagascar", "Os sem Floresta"]

#Tamanho da lista
print(len(filmeList))
#Recuperando intem  da lista pelo nome
print(filmeList.index("DeadPool"))
#Adicionando valor no final da lista
filmeList.append("Esquadrão Classe A")
print(filmeList)
# Ordena a Lista 
filmeList.sort()
print(filmeList)
# copia os itens de uma lista para a outra
filmesCopy = filmeList.copy()
filmesCopy.remove("DeadPool")
print(filmesCopy)
#remover todos os itens da lista
filmeList.clear()
print(filmeList)