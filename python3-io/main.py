f = open("./dados/contatos-novo.csv", encoding="latin_1", mode="r+")

contatos = [
    "11,Carol,carol@carol.com.br\n",
    "12,Ana,ana@ana.com.br\n",
    "13,Tais,tais@tais.com.br\n",
    "14,Felipe,felipe@felipe.com.br\n",
]

for contato in contatos:
    f.write(contato)

# f.seek(26)

# f.write("Teste\n")
# f.write("Teste\n")
