import re


class Extrator_url:
    def __init__(self, url, taxa):
        self.url = self.sanitizador_url(url)
        self.valida_url()
        self.taxa = taxa

    def sanitizador_url(self, url):
        if type(url) == str:
            return url.strip()
        else:
            return ""

    def valida_url(self):
        if not self.url:
            raise ValueError("A URL está vazia!")

        padrao_url = re.compile("(http(s)?://)?(www.)?bytebank.com(.br)?/cambio")
        match = padrao_url.match(self.url)
        if not match:
            raise ValueError("A URL não é válida!")

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

    def __get_valor_parametro(self, parametro):
        indice_parametro = self.url_parametros.find(parametro)
        indice_valor = indice_parametro + len(parametro) + 1
        indice_e_comercial = self.url_parametros.find("&", indice_valor)
        if indice_e_comercial == -1:
            valor = self.url_parametros[indice_valor:]
        else:
            valor = self.url_parametros[indice_valor:indice_e_comercial]
        return valor

    @property
    def valor_origem(self):
        return self.__get_valor_parametro("moedaOrigem")

    @property
    def valor_destino(self):
        return self.__get_valor_parametro("moedaDestino")

    @property
    def valor_quantidade(self):
        return self.__get_valor_parametro("quantidade")

    def __validador_cambio(self):
        if (self.valor_origem == "real" and self.valor_destino == "dolar") or (
            self.valor_origem == "dolar" and self.valor_destino == "real"
        ):
            return True
        else:
            raise Exception(
                f"O câmbio de {self.valor_origem} para {self.valor_destino} não está disponível"
            )

    @property
    def valor_conversao(self):
        self.__validador_cambio()
        quantidade = float(self.valor_quantidade)
        conversao = (
            f"O valor de ${quantidade:.2f} dolares em reais é R${quantidade * self.taxa :.2f}"
            if self.valor_origem == "dolar"
            else f"O valor de R${quantidade:.2f} reais em dolares é ${quantidade / self.taxa :.2f}"
        )
        return conversao

    def __len__(self):
        return len(self.url)

    def __str__(self):
        return f"{self.url}\nURL Base: {self.url_base}\nParâmetros da URL: {self.url_parametros}"

    def __eq__(self, other):
        return self.url == other.url


extrator = Extrator_url(
    "https://bytebank.com/cambio?moedaOrigem=real&moedaDestino=dolar&quantidade=200",
    5.5,
)

print(extrator.valor_conversao)
