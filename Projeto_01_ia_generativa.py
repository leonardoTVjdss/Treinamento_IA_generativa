# Importe a LIB da OpenAI
import openai

# Declarar a chave da OpenAI
openai.api_key = "Cole_Sua_KEY"

# Definir o prompt
prompt = """

    Voce e um product Owner de uma grande empresa de telecomunicações e voce trabalha com o produto de fibra.

    voce deve auxiliar os colaboradores na etapa de quebra de requisitos de uma feature que sera desenvolvida, todo
    feature precisa ter no minimo 5 requisitos, voce recebere pedidos de ajuda e voce deve devolver sempre neste 
    formato a seguir:

    **requisito 1**
    Prioridade - Alta, media ou baixa
    tempo estimado - em sprints
    descricao - descricao do requisito
    criterio de aceite - definir criterio de aceite  

"""

# Definir a pergunta
pergunta="""

    Estou em um projeto que vai alavancar as vendas de fibra nas cidades do interior, para isso eu vou criar
    um sistema que consiga analisar melhor a disponibilidade de fibra nas cidades do interior, me ajude a quebrar
    em requisitos funcionais para que eu possa criar esse sistema.

"""

# Definir o modelo
chat = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    temperature=0.7,
    max_tokens=1000,
    top_p=0.95,
    messages=[{
        "role": "system",
        "content": f"{prompt}"
    },
    {
        "role": "user",
        "content": f"{pergunta}"
    }]
)

# imprimir a resposta
resposta = chat.choices[0].message.content
print(resposta)
