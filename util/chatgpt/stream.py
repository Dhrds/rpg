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
        stream=True
    )
    return response


def main():
    response = enviar("me fale sobre a api do chatgpt")
    print(response)
    for chunk in response:
        if chunk.choices[0].delta.content is not None:
            print(chunk.choices[0].delta.content, end="")


if __name__ == "__main__":
    main()
