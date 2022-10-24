class Conta:
    def __init__(self, numero, titular, saldo, limite):

        print("Construindo um objeto ...")
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def extrato(self):
        print("O saldo do titular {} é R${:.2f}".format(self.__titular, self.__saldo))

    def depositar(self, valor):
        self.__saldo += valor

    def __credito_disponivel(self, valor_a_sacar):
        credito_total = self.__saldo + self.__limite
        return valor_a_sacar <= credito_total

    def sacar(self, valor):
        if self.__credito_disponivel(valor):
            self.__saldo -= valor
        else:
            print(
                "Você não possui crédito suficiente para sacar o valor de R${:.2f}.".format(
                    valor
                )
            )

    def transferir(self, valor, destino):
        self.sacar(valor)
        destino.depositar(valor)

    @property
    def numero(self):
        return self.__numero

    @property
    def titular(self):
        return self.__titular

    @property
    def saldo(self):
        return self.__saldo

    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self, novo_limite):
        self.__limite = novo_limite

    @staticmethod
    def codigo_banco():
        return "001"

    @staticmethod
    def codigos_dos_bancos():
        return {"BB": "001", "Caixa": "104", "Bradesco": "237"}
