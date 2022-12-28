import re


class Telefone:
    def __init__(self, numero):
        numero = str(numero)
        self._valida(numero)

    def __str__(self):
        return self._format()

    def _valida(self, numero):
        padrao = r"(\d{2,3}?)?(\d{2})(9?)(\d{8}$)"
        telefone = re.search(padrao, numero)
        if telefone:
            self._telefone = numero
        else:
            raise ValueError("Telefone inválido!")

    def _format(self):
        padrao = r"(\d{2,3}?)?(\d{2})(9?)(\d{4})(\d{4}$)"
        telefone = re.search(padrao, self._telefone)
        if telefone.group(1) == None and telefone.group(3) == None:
            return f"({telefone.group(2)}){telefone.group(4)}-{telefone.group(5)}"
        elif telefone.group(1) == None:
            return f"({telefone.group(2)}){telefone.group(3)}{telefone.group(4)}-{telefone.group(5)}"
        elif telefone.group(3) == None:
            return f"+{telefone.group(1)}({telefone.group(2)}){telefone.group(4)}-{telefone.group(5)}"
        else:
            return f"+{telefone.group(1)}({telefone.group(2)}){telefone.group(3)}{telefone.group(4)}-{telefone.group(5)}"
