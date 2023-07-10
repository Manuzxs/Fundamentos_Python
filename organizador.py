import os

def option(function):
    return function

user = input("Qual é o seu nome? ")
print(f"Hello, {user}! \nEscolha um número no menu e depois digite aqui.")
while True:
    menu = input("1. Criar pasta\n2. Deletar pasta\n3. Criar arquivo\n4. Deletar arquivo\n5. Editar arquivo\n")
    name = input("Tipe the Name: ")
    if menu == "1":
        option(os.mkdir(name))
    elif menu == "2":
        option(os.rmdir(name))
    elif menu == "3":
        with open(name, "w", encoding="UTF-8") as file:
            file.write("Bem vindo a seu arquivo, nele você pode escrever tudo o que você quiser!")
    elif menu == "4":
        option(os.rm(name))
    elif menu == "5":
        with open(name, "a", encoding="UTF-8") as file:
            file.write("\nBem vindo a seu arquivo, nele você pode escrever tudo o que você quiser!")