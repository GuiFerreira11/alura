try:
    with open("./dados/contatos-novo.csv", encoding="latin_1", mode="r+") as file:
        for line in file:
            print(line, end="")
except FileNotFoundError:
    print("Arquivo não encontrado")
except PermissionError:
    print("Permissão de acesso negada")
