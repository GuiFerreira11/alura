

class Conta:

    def __init__(self, numero, titular, saldo, limite):
        self.numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def extrato(self):
        print('O saldo do titular {} é de R$ {:.2f}'.format(self.__titular, self.__saldo))

    def deposita(self, valor):
        self.__saldo += valor
        print('Depósito efetuado.')

    def __pode_sacar(self, valor_a_sacar):
        valor_disponivel_a_sacar = self.__saldo + self.__limite
        return valor_a_sacar <= valor_disponivel_a_sacar

    def saca(self, valor):
        if self.__pode_sacar(valor):
            self.__saldo -= valor
            print('Saque efetuado.')
        else:
            print('Você não possui saldo suficente, o valor R$ {:.2f} ultrapassou o limite.'.format(valor))

    def transfere(self, valor, destino):
        if self.__pode_sacar(valor):
            self.__saldo -= valor
            destino.deposita(valor)
            print('Transferência efetuada.')
        else:
            print('Você não possui saldo suficente, o valor R$ {:.2f} ultrapassou o limite.'.format(valor))

    @property
    def saldo(self):
        return self.__saldo

    @property
    def titular(self):
        return self.__titular

    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self, limite):
        self.__limite = limite

    @staticmethod
    def codigo_banco():
        return '001'

    @staticmethod
    def codigos_bancos():
        return {'BB': '001', 'Caixa': '104', 'Bradesco': '237'}
