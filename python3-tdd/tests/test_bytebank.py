from codigo.bytebank import Funcionario


class TestClass:
    def test_quando_idade_recebe_13_03_2000_deve_retornar_23(self):
        entrada = "13/03/2000"  # Given-contexto
        esperado = 23

        funcionario_teste = Funcionario("Teste", entrada, 1000)
        resposta = funcionario_teste.idade()  # When-ação

        assert resposta == esperado  # Then-desfecho

    def test_quando_sobrenome_recebe_Lucas_Carvalho_deve_retornar_Carvalho(self):
        entrada = " Lucas teste Carvalho "  # Given
        esperado = "Carvalho"

        funcionario_teste = Funcionario(entrada, "13/03/2000", 1000)
        resposta = funcionario_teste.sobrenome()  # When

        assert resposta == esperado  # Then
