from validate_docbr import CPF, CNPJ


class Documeto:
    @staticmethod
    def cria_documento(tipo: str, documento):
        documento = str(documento)
        if tipo == "cpf":
            return cpf(documento)
        elif tipo == "cnpj":
            return cnpj(documento)
        else:
            raise ValueError("Documento não inválido!")


class cnpj:
    def __init__(self, documento):
        self._valida(documento)

    def __str__(self):
        return self._format()

    def _valida(self, cnpj):
        if len(cnpj) == 14:
            validador = CNPJ()
            if validador.validate(cnpj):
                self._cnpj = cnpj
            else:
                raise ValueError("CNPJ inválido!")
        else:
            raise ValueError("Quantidade de dígitos no CNPJ inválido!")

    def _format(self):
        cnpj = CNPJ()
        return cnpj.mask(self._cnpj)


class cpf:
    def __init__(self, documento):
        self._valida(documento)

    def __str__(self):
        return self._format()

    def _valida(self, cpf):
        if len(cpf) == 11:
            validador = CPF()
            if validador.validate(cpf):
                self._cpf = cpf
            else:
                raise ValueError("CPF inválido!")
        else:
            raise ValueError("Quantidade de dígitos no CPF inválido!")

    def _format(self):
        cpf = CPF()
        return cpf.mask(self._cpf)
