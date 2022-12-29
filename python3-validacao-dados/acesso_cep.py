import requests


class Busca_endereco:
    def __init__(self, numero):
        numero = str(numero)
        self._valida(numero)

    @property
    def cep(self):
        return self._format()

    def __str__(self):
        return self._acessa_via_cep()

    def _valida(self, numero):
        if len(numero) == 8:
            self._cep = numero
        else:
            raise ValueError("CEP inválido!")

    def _format(self):
        return f"{self._cep[:5]}-{self._cep[5:]}"

    def _acessa_via_cep(self):
        url = f"https://viacep.com.br/ws/{self._cep}/json/"
        r = requests.get(url)
        dados = r.json()
        cep = dados["cep"]
        logradouro = dados["logradouro"]
        complemento = dados["complemento"]
        bairro = dados["bairro"]
        localidade = dados["localidade"]
        uf = dados["uf"]
        endereco = f"{logradouro}{complemento}, {bairro}, {localidade} - {uf} - {cep}"
        return endereco
