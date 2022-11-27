url = "https://bytebank.com/cambio?moedaOrigem=real&moedaDestino=dolar&quantidade=100"
print(url)

indice_interrogacao = url.find("?")

url_base = url[:indice_interrogacao]
print(url_base)

url_parametro = url[: indice_interrogacao + 1 :]
print(url_parametro)

print(url)
