import os
import openai
from django.shortcuts import render
from .models import Aventura, Personagem
openai.api_key = os.getenv("OPENAI_API_KEY")


def enviar(mensagem, id=int, lista_mensagens=[], reiniciar=False):
    personagem = Personagem.objects.get(id=id)
    exemplo = f"""
            <h1>Combate Épico - Enterrem seus medos na escuridão da caverna</h1>
            Você se encontra nas profundezas de uma caverna sombria,
            cujas paredes de pedra se estendem pela escuridão como sentinelas antigas.
            O cheiro de mofo e abandono paira no ar,
            misturado com o eco distante de goteiras que ressoam pelas galerias vazias. 
            {personagem.ficha['nome']}, 
            avança com passos cautelosos, seu instinto aguçado pela presença de perigo iminente.
            Seu arco longo preparado, uma flecha mágica envolta em energia arcanas pronta para ser disparada.
            Em meio às sombras dançantes, um rosnado gutural ecoa pela caverna, seguido pelo surgimento furtivo de um goblin.
            A criatura de pele verde e olhos ardilosos segura uma lança improvisada, pronta para o combate.
            O goblin avança em sua direção, dentes à mostra em um sorriso cruel. O momento do confronto é iminente.
            <h3>Iniciativa:</h3>
            {personagem.ficha['nome']}: 15 - Goblin: 10
            <br><br>
            {personagem.ficha['nome']}, você age primeiro. O que deseja fazer? """ # noqa E501
    if reiniciar:
        lista_mensagens.clear()
    if not lista_mensagens:
        lista_mensagens.append(
            {
                "role": "system", "content":
                f"""
            Você sera um narrador de D&D.
            sera um combate entre o jogador e um goblin.
            o cenário escolhido é uma caverna que é uma prisão abandonada , 
            um lugar repleto de mistérios e perigos.
            quero que a formatação seja em html, com divisão de tópico com títulos em <h3>,
            a rolagem de dados formatada e com quebras de linhas com <br>
            termine a resposta com uma ação do adversário.
            lembre de mostrar o quanto resta de vida tanto do personagem e da criatura.
            quando derrotar a criatura recompense com um item e comece outro combate.
            
            Preparem-se para uma jornada épica, onde a coragem e a astúcia serão testadas ao limite.
            Que suas escolhas moldem o destino deste mundo e que suas proezas sejam cantadas por gerações.
            
            
        
            a ficha do jogador é {personagem.ficha}
                lembre-se do torno da criatura se ela ainda estiver viva.
                nível de dificuldade = alto
                """ # noqa E501
            }
        )
        lista_mensagens.append(
            {"role": "assistant", "content": f'''
            <h1>Combate Épico - Enterrem seus medos na escuridão da caverna</h1>
            Você se encontra nas profundezas de uma caverna sombria,
            cujas paredes de pedra se estendem pela escuridão como sentinelas antigas.
            O cheiro de mofo e abandono paira no ar,
            misturado com o eco distante de goteiras que ressoam pelas galerias vazias. 
            {personagem.ficha['nome']}, 
            avança com passos cautelosos, seu instinto aguçado pela presença de perigo iminente.
            Em meio às sombras dançantes, um rosnado gutural ecoa pela caverna, seguido pelo surgimento furtivo de um goblin.
            A criatura de pele verde e olhos ardilosos segura uma lança improvisada, pronta para o combate.
            O goblin avança em sua direção, dentes à mostra em um sorriso cruel. O momento do confronto é iminente.
            <h3>Iniciativa:</h3>
            {personagem.ficha['nome']}: 15 - Goblin: 10
            <br><br>
            você age primeiro. O que deseja fazer?
            ''' # noqa E501
             })
    if mensagem:
        lista_mensagens.append(
            {"role": "user", "content": mensagem})

        if not reiniciar:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=lista_mensagens,
            )
            lista_mensagens.append(response["choices"][0]["message"])

    return lista_mensagens, personagem, exemplo


def jogo_rpg(request):

    if request.method == 'GET':
        id_personagem = int(request.GET.get('id', 1))
        response = enviar('', id_personagem)
        return render(request, 'chat.html', {'resposta': response[0],
                                             'personagem': response[1]})

    else:
        mensagem_atual = request.POST.get('mensagem', '')
        reiniciar = bool(request.POST.get('reiniciar', False))
        salvar = bool(request.POST.get('salvar', False))
        id_personagem = int(request.GET.get('id', 1))
        response = enviar(mensagem_atual, id_personagem, reiniciar=reiniciar)
        if salvar:
            historia = Aventura(json=response[0])
            historia.save()
        print(response[1])
        return render(request, 'chat.html', {
            'resposta': response[0],
            'personagem': response[1]})


def home(request):
    personagens = Personagem.objects.all()
    return render(request, 'index.html', {'personagens': personagens})
