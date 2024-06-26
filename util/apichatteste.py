import openai
import os
openai.api_key = os.getenv("OPENAI_API_KEY")


def enviar(mensagem, lista_mensagens=[]):
    lista_mensagens.append(
        {"role": "user", "content": mensagem}
        )

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=lista_mensagens,
    )
    lista_mensagens.append(response["choices"][0]["message"])

    return response["choices"][0]["message"]['content']


if __name__ == "__main__":
    while (True):
        resposta = enviar(input("Digite uma mensagem: "))
        print(resposta)
