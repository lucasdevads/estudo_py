filmeSimpsons = {
    "titulo": "Os Simpsons",
    "ano": 2013,
    "nota": 9.0,
    "genero": "animação"
}

print(filmeSimpsons)
print(len(filmeSimpsons))
print(type(filmeSimpsons))

# recupera um elemento do dicionario
print(filmeSimpsons["genero"])
print(filmeSimpsons.get("ano"))

# busca apenas as chave do dicionario
print(filmeSimpsons.keys())

# buscando apenas os valores dos dicionarios

print(filmeSimpsons.values())

# buscar item do dicionario com chave e valor
print(filmeSimpsons.items())

# adicionar itens no dicionario
filmeSimpsons["diretor"] = "David silverman"
print(filmeSimpsons)

#atualizar itens no dicionario
filmeSimpsons.update({"nota": 9.5}) 
print(filmeSimpsons)