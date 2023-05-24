import os

nome = input("Qual é o seu nome? ")
print(f"Hello, {nome}! \nEscolha um número no menu e depois digite aqui.")

menu = input("1. Criar pasta\n2. Deletar pasta\n")
if menu == "1":
    nome_pasta = input("Nome da pasta: ")
    os.mkdir(nome_pasta)
elif menu == "2":
    nome_pasta = input("Nome da pasta: ")
    os.rmdir(nome_pasta)