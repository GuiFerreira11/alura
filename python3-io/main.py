import contato_utils

try:
    # contatos = contato_utils.contato_for_csv("./dados/contatos.csv")
    # contato_utils.contatos_to_pickle(contatos, "./dados/contatos.pickle")

    # contatos = contato_utils.pickle_to_contatos("./dados/contatos.pickle")
    # contato_utils.contatos_to_json(contatos, "./dados/contatos.json")

    contatos = contato_utils.json_to_contatos("./dados/contatos.json")

    for contato in contatos:
        print(f"{contato.id} - {contato.nome} - {contato.email}")
except FileNotFoundError:
    print("Arquivo não encontrado")
except PermissionError:
    print("Permissão de acesso negada")
