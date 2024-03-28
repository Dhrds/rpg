from django.shortcuts import HttpResponse, redirect
from openai import OpenAI
import os

api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)


def gera_img(request):

    if request.method == 'POST':
        texto = request.POST.get('promt')
        response = client.images.generate(
            model="dall-e-3",
            prompt=texto,
            size="1024x1024",
            quality="standard",
            n=1,
        )

        image_url = response.data[0].url
        return redirect(image_url)
    return HttpResponse('''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Formulário Django</title>
    </head>
    <body>
        <h1>Formulário Django</h1>
        <form method="post" action="{% url 'processar_formulario' %}">
            {% csrf_token %}
            <label for="nome">promt:</label><br>
            <input type="text" id="promt" name="promt"><br>
            <input type="submit" value="Enviar">
        </form>
    </body>
    </html>
                        ''')
