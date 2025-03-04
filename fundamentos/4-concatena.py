
nome = input("Digite o nome do filme: \n")
anoLancamento = int(input("Digite o ano de lancamento do filme: \n"))
notaFilme = float(input("Digite uma nota para o Filme: \n"))

print("Dados do Filme.")
print("======================")
# alternativa 01
# print("Nome do Filme :", nome)
# print("Ano do Filme:", anoLancamento)
# print("Nota do Filme :", notaFilme)

# # alternativa 02
# print("Nome do Filme:", nome, "\nAno de lançamento: ", anoLancamento, "\nNota do filme: ", notaFilme)

# alternativa 03
print(f"Nome do Filme: {nome}\n"
      f"Ano Lançamento {anoLancamento}\n"
        f"nota do filma: {notaFilme}")