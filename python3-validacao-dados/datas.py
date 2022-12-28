from datetime import datetime


class Datas:
    def __init__(self):
        self._momento_cadastro = datetime.today()

    def __str__(self):
        return self._format()

    def mes_cadastro(self):
        meses = [
            "Janeiro",
            "Fevereiro",
            "Março",
            "Abril",
            "Maio",
            "Junho",
            "Julho",
            "Agosto",
            "Setembro",
            "Outubro",
            "Novembro",
            "Dezembro",
        ]
        mes = self._momento_cadastro.month - 1
        return meses[mes]

    def dia_semana(self):
        dias_semana = [
            "Segunda-Feira",
            "Terça-Feira",
            "Quarta-Feira",
            "Quinta-Feira",
            "Sexta-Feira",
            "Sabado",
            "Domingo",
        ]
        dia_semana = self._momento_cadastro.weekday()
        return dias_semana[dia_semana]

    def _format(self):
        data_formatada = self._momento_cadastro.strftime("%d/%m/%Y %H:%M")
        return self.dia_semana() + " " + data_formatada

    def tempo_cadastrado(self):
        return datetime.today() - self._momento_cadastro
