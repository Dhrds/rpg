from django.shortcuts import HttpResponse, redirect
import openai
import os
from django.shortcuts import render

api_key = os.getenv("OPENAI_API_KEY")
client = openai.api_key = api_key


def gera_img(request):

    if request.method == 'POST':
        texto = request.POST.get('promt')
        response = openai.Image.create(
            model="dall-e-3",
            prompt=texto,
            size="1024x1024",
            quality="standard",
            n=1,
        )

        image_url = response.data[0].url
        return redirect(image_url)
    return render(request, 'gerar.html')
