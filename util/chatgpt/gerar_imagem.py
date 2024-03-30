from openai import OpenAI
import os
import base64

api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)


def gerar_imagem(texto):

    response = client.images.generate(
      model="dall-e-3",
      prompt=texto,
      size="1024x1024",
      quality="standard",
      response_format="b64_json",
      n=1,
    )

    # image_url = response.data[0].url
    image_data = response.data[0].b64_json
    img = base64.b64decode(image_data)
    with open(f"image{texto}.png", "wb") as f:
        f.write(img)
        print("Imagem salva com sucesso!")


def editar_imagem(texto):
    with open("imageum site parajogar D&D.png", "rb") as image_file:
        with open("mask.png", "rb") as mask_file:
            response = client.images.edit(
                image=image_file,
                mask=mask_file,
                prompt=texto,
                n=1,
                size="1024x1024",
                response_format="b64_json",
            )

    image_data = response.data[0].b64_json
    img = base64.b64decode(image_data)
    with open("img.png", "wb") as f:
        f.write(img)
        print("Imagem salva com sucesso!")


# editar_imagem('em preto e branco')
gerar_imagem('um site parajogar D&D')