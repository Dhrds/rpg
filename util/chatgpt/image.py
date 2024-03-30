import openai
import os
# flake8: noqa E501
openai.api_key = os.getenv("OPENAI_API_KEY")


response = openai.Image.create(
  model="dall-e-3",
  prompt="",
  size="1024x1024",
  quality="standard",
  n=1,
)

image_url = response.data[0].url
print(image_url)
