import re


class Extrator_url:
    def __init__(self, url, taxa=5.5):
        self.url = self.__sanitizador_url(url)
        self.__valida_url()
        self.__taxa = taxa

    def __sanitizador_url(self, url):
        if type(url) == str:
            return url.strip()
        else:
            return ""

    def __valida_url(self):
        if not self.url:
            raise ValueError("A URL está vazia!")

        padrao_url = re.compile("(http(s)?://)?(www.)?bytebank.com(.br)?/cambio")
        match = padrao_url.match(self.url)
        if not match:
            raise ValueError("A URL não é válida!")

    @property
    def taxa(self):
        return self.__taxa

    @taxa.setter
    def taxa(self, nova_taxa):
        self.__taxa = nova_taxa

    @property
    def __indice_separador_base_parametros(self):
        indice = self.url.find("?")
        return indice

    @property
    def url_base(self):
        return self.url[: self.__indice_separador_base_parametros]

    @property
    def url_parametros(self):
        return self.url[self.__indice_separador_base_parametros + 1 :]

    def __valor_parametro(self, parametro):
        indice_parametro = self.url_parametros.find(parametro)
        assert indice_parametro != -1, f"O parâmetro {parametro} não foi encontrado"
        indice_valor = indice_parametro + len(parametro) + 1
        indice_e_comercial = self.url_parametros.find("&", indice_valor)
        if indice_e_comercial == -1:
            valor = self.url_parametros[indice_valor:]
        else:
            valor = self.url_parametros[indice_valor:indice_e_comercial]
        return valor

    @property
    def moeda_origem(self):
        return self.__valor_parametro("moedaOrigem")

    @property
    def moeda_destino(self):
        return self.__valor_parametro("moedaDestino")

    @property
    def valor_para_converter(self):
        return self.__valor_parametro("quantidade")

    def __validador_cambio(self):
        if (self.moeda_origem == "real" and self.moeda_destino == "dolar") or (
            self.moeda_origem == "dolar" and self.moeda_destino == "real"
        ):
            return True
        else:
            raise Exception(
                f"O câmbio de {self.moeda_origem} para {self.moeda_destino} não está disponível"
            )

    @property
    def valor_convertido(self):
        self.__validador_cambio()
        quantidade = float(self.valor_para_converter)
        conversao = (
            f"O valor de ${quantidade:.2f} dolares em reais é R${quantidade * self.taxa :.2f}"
            if self.moeda_origem == "dolar"
            else f"O valor de R${quantidade:.2f} reais em dolares é ${quantidade / self.taxa :.2f}"
        )
        return conversao

    def __len__(self):
        return len(self.url)

    def __str__(self):
        return f"{self.url}\nURL Base: {self.url_base}\nParâmetros da URL: {self.url_parametros}"

    def __eq__(self, other):
        return self.url == other.url
