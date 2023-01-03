from bytebank import Funcionario


def teste_idade():
    funcionario_teste = Funcionario("Teste", "31/12/1995", 1100)
    print(f"Teste = {funcionario_teste.idade()}")


teste_idade()
