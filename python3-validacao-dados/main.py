from doc import Documeto
from telefone import Telefone
from datas import Datas
from acesso_cep import Busca_endereco

documento_1 = Documeto.cria_documento("cnpj", 32815361000182)
documento_2 = Documeto.cria_documento("cpf", 57358746082)
celular = Telefone(5511964890345)
cadastro = Datas()
endereco = Busca_endereco(89036610)

print(documento_1)
print(documento_2)
print(celular)
print(cadastro)
print(endereco)
