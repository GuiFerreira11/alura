from codigo.bytebank import Funcionario
import pytest


class TestClass:
    # @pytest.mark.skip
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

    def test_quando_reducao_salario_recebe_100000_deve_retornar_90000(self):
        entrada_nome = "Paulo Bragança"
        entrada_salario = 100000  # Given
        esperado = 90000

        funcionario_teste = Funcionario(entrada_nome, "13/03/2000", entrada_salario)
        funcionario_teste.reducao_salario()  # When
        resposta = funcionario_teste.salario

        assert resposta == esperado  # Then

    @pytest.mark.bonus
    def test_quando_calcular_bonus_recebe_1000_deve_retornar_100(self):
        entrada = 1000  # Given
        esperado = 100

        funcionario_teste = Funcionario("Teste", "13/03/2000", entrada)
        resposta = funcionario_teste.calcular_bonus()  # When

        assert resposta == esperado  # Then

    @pytest.mark.bonus
    def test_quando_calcular_bonus_recebe_100000_deve_retornar_exception(self):
        with pytest.raises(Exception):
            entrada = 100000  # Given

            funcionario_teste = Funcionario("Teste", "13/03/2000", entrada)
            resposta = funcionario_teste.calcular_bonus()  # When

            assert resposta  # Then
