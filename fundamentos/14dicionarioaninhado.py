import pprint

filmesDict = {
    "os simpsons":{
        "ano": 2013,
        "nota": 9.0,
        "genero": "animação"},

    "Esquadrão Classe A":{
        "ano": 2013,
        "nota": 8.0,
        "genero": "ação"},

    "Blade":{
        "ano": 2010,
        "nota": 9.0,
        "genero": "ação"},
}

pp = pprint.PrettyPrinter(depth=4)

pp.pprint(filmesDict)

# buscar uma informação dentro de um dicionario aninhado

print(filmesDict["Blade"]["genero"])

# Adicionar um novo item
filmesDict["os simpsons"]["diretor"] = "David"

print(filmesDict["os simpsons"])
print()
# excluir um dicionario
del filmesDict["Blade"]

pp.pprint(filmesDict)