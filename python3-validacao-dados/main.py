from doc import Documeto
from telefone import Telefone

documento_1 = Documeto.cria_documento("cnpj", 15008735000139)
documento_2 = Documeto.cria_documento("cpf", 42304877893)

print(documento_1)
print(documento_2)

celular = Telefone(5511994040060)
print(celular)
