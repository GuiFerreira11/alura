# url = "https://bytebank.com/cambio?moedaOrigem=real&moedaDestino=dolar&quantidade=100"
url = " "

# Sanitizacao
url = url.strip()

# Validacao da URL
if url == "":
    raise ValueError("A URL está vazia!")

# Seprara a base dos parametros
indice_interrogacao = url.find("?")
url_base = url[:indice_interrogacao]
url_parametro = url[indice_interrogacao + 1 :]


# Busca por um parametro
# parametro_busca = "quantidade"
parametro_busca = "moedaDestino"
# parametro_busca = "moedaOrigem"
indice_parametro = url_parametro.find(parametro_busca)
indice_valor = indice_parametro + len(parametro_busca) + 1
indice_e_comercial = url_parametro.find("&", indice_valor)

if indice_e_comercial == -1:
    valor = url_parametro[indice_valor:]
else:
    valor = url_parametro[indice_valor:indice_e_comercial]

print(valor)
