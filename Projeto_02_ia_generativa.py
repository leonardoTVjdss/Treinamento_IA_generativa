# Importar a Lib OpenAI
import openai

# Receber a chave da OpenAI
openai.api_key = "Cole_a_key"

# Definir o prompt
prompt = """

    Você é um analista de negocios renomado com 10 anos de experiencia, e que trabalha com custumer success, na montadora volkswagen.

    voce vai receber perguntas de clientes sobre os veiculos da volkswagen, os tipos de perguntas serao variados, como pontencia, torque, velocidade maxima etc.

"""

# Criar um sistema de chatbot com IA
print('-'*30)
print('Olá, seja bem vindo ao chatbot da Volkswagen!')
print('-'*30)

# Laço de repetição
opcao = 0
while opcao != 2:
    pergunta = str(input("Digite sua pergunta:"))

    # Definir o modelo
    chat = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        temperature=0.7,
        messages=[{
        "role": "system",
        "content": f"{prompt}"
    },
    {
        "role": "user",
        "content": f"{pergunta}"
    }])

    # imprimir a resposta
    resposta = chat.choices[0].message.content
    print("\n", resposta, "\n\nfim da resposta\n\n")
    print('-'*30)

    # Menu de opcoes
    opcao = int(input("Deseja fazer mais uma pergunta? 1 - Sim 2 - Não: "))
    if opcao != 2:
        print("\n")
    elif opcao == 2:
        print('-'*30)
        print("Obrigado por utilizar o chatbot da Volkswagen!")
        print('-'*30)

# fim de programa
