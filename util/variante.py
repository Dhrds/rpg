from openai import OpenAI
import os

api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)
response = client.images.create_variation(
#   model="dall-e-3",
  image=open(r"C:\Users\douglas\Desktop\git\rpg\rpg\util\1.png", "rb"),
#   prompt="""ilustração MULHER forte CaRREGANDO O MUNDO NAS COSTAS REPRESENTANDO A SOBRECARGA DA MULHER MODERNA,
#   caracteristica da mulher cabelo preso, roupas social, com olheiras, pensamentos acelerados
#   , 
#   """,
  size="1024x1024",
#   quality="standard",
  n=1,
)

image_url = response.data[0].url
print(image_url)
