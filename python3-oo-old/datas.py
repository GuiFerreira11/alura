

class Data:

    def __init__(self, dia, mes, ano):
        self.d = dia
        self.m = mes
        self.a = ano

    def formatada(self):
        print('{}/{}/{}'.format(self.d, self.m, self.a))
