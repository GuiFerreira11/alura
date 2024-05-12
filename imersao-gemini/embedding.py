from google.generativeai import embedding
from google.generativeai.text import models
import numpy as np
import pandas as pd
import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

api_key = str(os.getenv("API_KEY"))

genai.configure(api_key=api_key)

# for m in genai.list_models():
#     if "embedContent" in m.supported_generation_methods:
#         print(m.name)

# text = "Hello World"
#
# resultado = genai.embed_content(model="models/embedding-001", content=text)
#
# print(resultado)

# resultado = genai.embed_content(model="models/embedding-001", content=[
#     "What is the meaning of life?",
#     "How much wood would a woodchuck chuck?",
#     "How does the brain work?"
#     ])
#
# for embedding in resultado["embedding"]:
#     print(embedding)

DOCUMENT1 = {
    "Título": "Operação do sistema de controle climático",
    "Conteúdo": "O Googlecar tem um sistema de controle climático que permite ajustar a temperatura e o fluxo de ar no carro. Para operar o sistema de controle climático, use os botões e botões localizados no console central.  Temperatura: O botão de temperatura controla a temperatura dentro do carro. Gire o botão no sentido horário para aumentar a temperatura ou no sentido anti-horário para diminuir a temperatura. Fluxo de ar: O botão de fluxo de ar controla a quantidade de fluxo de ar dentro do carro. Gire o botão no sentido horário para aumentar o fluxo de ar ou no sentido anti-horário para diminuir o fluxo de ar. Velocidade do ventilador: O botão de velocidade do ventilador controla a velocidade do ventilador. Gire o botão no sentido horário para aumentar a velocidade do ventilador ou no sentido anti-horário para diminuir a velocidade do ventilador. Modo: O botão de modo permite que você selecione o modo desejado. Os modos disponíveis são: Auto: O carro ajustará automaticamente a temperatura e o fluxo de ar para manter um nível confortável. Cool (Frio): O carro soprará ar frio para dentro do carro. Heat: O carro soprará ar quente para dentro do carro. Defrost (Descongelamento): O carro soprará ar quente no para-brisa para descongelá-lo."}

DOCUMENT2 = {
    "Título": "Touchscreen",
    "Conteúdo": "O seu Googlecar tem uma grande tela sensível ao toque que fornece acesso a uma variedade de recursos, incluindo navegação, entretenimento e controle climático. Para usar a tela sensível ao toque, basta tocar no ícone desejado.  Por exemplo, você pode tocar no ícone \"Navigation\" (Navegação) para obter direções para o seu destino ou tocar no ícone \"Music\" (Música) para reproduzir suas músicas favoritas."}

DOCUMENT3 = {
    "Título": "Mudança de marchas",
    "Conteúdo": "Seu Googlecar tem uma transmissão automática. Para trocar as marchas, basta mover a alavanca de câmbio para a posição desejada.  Park (Estacionar): Essa posição é usada quando você está estacionado. As rodas são travadas e o carro não pode se mover. Marcha à ré: Essa posição é usada para dar ré. Neutro: Essa posição é usada quando você está parado em um semáforo ou no trânsito. O carro não está em marcha e não se moverá a menos que você pressione o pedal do acelerador. Drive (Dirigir): Essa posição é usada para dirigir para frente. Low: essa posição é usada para dirigir na neve ou em outras condições escorregadias."}

documents = [DOCUMENT1, DOCUMENT2, DOCUMENT3]

df = pd.DataFrame(documents)
df.columns = ["Titulo", "Conteudo"]

embed_model = "models/embedding-001"

def embedding_fn(modelo, title, text):
    return genai.embed_content(model=modelo,
                               content=text,
                               title=title,
                               task_type="RETRIEVAL_DOCUMENT")["embedding"]

df["Embedding"] = df.apply(lambda row: embedding_fn(embed_model, row["Titulo"], row["Conteudo"]), axis=1)

def gerar_e_buscar_consulta(modelo, consulta, database):
    embed_consulta = genai.embed_content(model=modelo,
                                         content=consulta,
                                         task_type="RETRIEVAL_QUERY")["embedding"]
    produtos_escalares = np.dot(np.stack(database["Embedding"]), embed_consulta)
    indice = np.argmax(produtos_escalares)
    return database.iloc[indice]["Conteudo"]

consulta = "Como se troca a marcha de um carro do google?"

resposta_consulta = gerar_e_buscar_consulta(embed_model, consulta, df)

generation_config = {
        "temperature": 1,
        "top_k": 20,
        "top_p": 0.75,
        "candidate_count": 1,
        }

safety = {
        "HARASSMENT": "BLOCK_NONE",
        "HATE": "BLOCK_NONE",
        "SEXUAL": "BLOCK_NONE",
        "DANGEROUS": "BLOCK_NONE",
        }

gen_model = "gemini-1.0-pro"

model = genai.GenerativeModel(
        model_name=gen_model,
        generation_config=generation_config,
        safety_settings=safety,
        )
prompt = f"Reescreva esse texto de uma forma mais simplificada, sem adicionar informações que não façam parte do texto: {resposta_consulta}"
resposta = model.generate_content(prompt)
print(resposta.text)
