import os

nome = input("Qual é o seu nome? ")
print(f"Hello, {nome}! \nEscolha um número no menu e depois digite aqui.")
while True:
    menu = input("1. Criar pasta\n2. Deletar pasta\n3. Criar arquivo\n4. Deletar arquivo\n5. Editar arquivo\n")
    if menu == "1":
        nome_pasta = input("Nome da pasta: ")
        os.mkdir(nome_pasta)
    elif menu == "2":
        nome_pasta = input("Nome da pasta: ")
        os.rmdir(nome_pasta)
    elif menu == "3":
        nome_arquivo = input("Nome da arquivo: ")
        with open(nome_arquivo, "w", encoding="UTF-8") as file:
            file.write("Bem vindo a seu arquivo, nele você pode ser tudo o que você quiser!")
    elif menu == "4":
        nome_arquivo = input("Nome da arquivo: ")
        os.rm(nome_arquivo)
    # elif menu == "5":
    #     # nome_arquivo = input("Nome da arquivo: ")
    #     # with open(nome_arquivo, "a", encoding="UTF-8") as file:
    #         # file.("Bem vindo a sua arquivo, nele você pode ser tudo o que você quiser!")
        
    #     l = [['The Hunger Games', 'Suzanne Collins', '12.97'],
    # ['The Fault In Our Stars', 'John Green', '11.76'],
    # ['The Notebook', 'Nicholas Sparks', '11.39']]
    #     with open('books.txt', 'r') as f:
    #         file = f.read()
    #         print(file)

        # with open('books.txt', 'w') as f:
        #     f.write('\n'.join([','.join(line) for line in l]))