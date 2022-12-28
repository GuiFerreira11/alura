from validate_docbr import CPF


class cpf:
    def __init__(self, documento):
        documento = str(documento)
        self._valida_cpf(documento)

    def __str__(self):
        return self._format_cpf()

    def _valida_cpf(self, cpf):
        if len(cpf) == 11:
            validador = CPF()
            if validador.validate(cpf):
                self._cpf = cpf
            else:
                raise ValueError("Documento inválido!")
        else:
            raise ValueError("Quantidade de dígito inválida!")

    def _format_cpf(self):
        cpf = CPF()
        return cpf.mask(self._cpf)
