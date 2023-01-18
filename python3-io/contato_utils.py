import csv, pickle, json
from contato import Contato


def contato_for_csv(path, encoding="latin_1"):
    contatos = []

    with open(path, encoding=encoding) as file:
        content = csv.reader(file)
        for line in content:
            id, nome, email = line

            contato = Contato(id, nome, email)
            contatos.append(contato)

    return contatos


def contatos_to_pickle(contatos, path):
    with open(path, mode="wb") as file:
        pickle.dump(contatos, file)


def pickle_to_contatos(path):
    with open(path, mode="rb") as file:
        contatos = pickle.load(file)
    return contatos


def contatos_to_json(contatos, path):
    with open(path, mode="w") as file:
        json.dump(contatos, file, default=_contato_to_dict)


def _contato_to_dict(contato):
    return contato.__dict__


def json_to_contatos(path):
    contatos = []

    with open(path) as file:
        contatos_json = json.load(file)

        for contato in contatos_json:
            c = Contato(**contato)
            contatos.append(c)

    return contatos
