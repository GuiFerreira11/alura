class Extrator_url:
    def __init__(self, url):
        self.url = self.sanitizador_url(url)
        self.valida_url()

    def sanitizador_url(self, url):
        if type(url) == str:
            return url.strip()
        else:
            return ""

    def valida_url(self):
        if not self.url:
            raise ValueError("A URL está vazia!")

    @property
    def indice_separador_base_parametros(self):
        indice = self.url.find("?")
        return indice

    @property
    def url_base(self):
        return self.url[: self.indice_separador_base_parametros]

    @property
    def url_parametros(self):
        return self.url[self.indice_separador_base_parametros + 1 :]

    def get_valor_parametro(self, parametro):
        indice_parametro = self.url_parametros.find(parametro)
        indice_valor = indice_parametro + len(parametro) + 1
        indice_e_comercial = self.url_parametros.find("&", indice_valor)
        if indice_e_comercial == -1:
            valor = self.url_parametros[indice_valor:]
        else:
            valor = self.url_parametros[indice_valor:indice_e_comercial]
        return valor


extrator = Extrator_url(
    "https://bytebank.com/cambio?moedaOrigem=real&moedaDestino=dolar&quantidade=100"
)
print(extrator.get_valor_parametro("quantidade"))
