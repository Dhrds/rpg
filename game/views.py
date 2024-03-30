from django.shortcuts import render
import openai
import os
# noqa E501  
openai.api_key = os.getenv("OPENAI_API_KEY")

jogador = {
        "nome": "Galadael",
        "raca": "Elfa da Lua",
        "classe": {
            "nome": "Ranger",
            "subclasse": "Arqueira Mística"
        },
        "atributos": {
            "forca": 14,
            "modificadorForca": 2,
            "destreza": 16,
            "modificadorDestreza": 3,
            "constituicao": 12,
            "modificadorConstituicao": 1,
            "inteligencia": 10,
            "modificadorInteligencia": 0,
            "sabedoria": 14,
            "modificadorSabedoria": 2,
            "carisma": 8,
            "modificadorCarisma": -1
        },
        "proficiencias": {
            "habilidades": [
                "Acrobacia",
                "Atletismo",
                "Percepcao",
                "Sobrevivencia"
            ],
            "armas": [
                "Adagas",
                "Arcos (longos, curtos)",
                ],
            },
        "equipamentos": [
            "Armadura de couro",
            "Arco longo",
            "Aljava com 20 flechas",
            "Adaga",
            "Kit de explorador",
            "Kit de herbalismo",
            "Roupas simples",
            "10 moedas de ouro",
            "50 moedas de prata"
            ],
        "magicas": {
            "primeiroNivel": [
                "Curar Feridas",
                "Detectar Magia",
                "Lançar Teia",
                "Projétil Mágico"
            ]
        },
        } # noqa E501
exemplo = f"""
<h1>Combate Épico - Enterrem seus medos na escuridão da caverna</h1>
Você se encontra nas profundezas de uma caverna sombria,
cujas paredes de pedra se estendem pela escuridão como sentinelas antigas.
O cheiro de mofo e abandono paira no ar,
misturado com o eco distante de goteiras que ressoam pelas galerias vazias. 
{jogador['nome']}, a destemida Elfa da Lua e Arqueira Mística, 
avança com passos cautelosos, seu instinto aguçado pela presença de perigo iminente.
Seu arco longo preparado, uma flecha mágica envolta em energia arcanas pronta para ser disparada.
Em meio às sombras dançantes, um rosnado gutural ecoa pela caverna, seguido pelo surgimento furtivo de um goblin.
A criatura de pele verde e olhos ardilosos segura uma lança improvisada, pronta para o combate.
O goblin avança em sua direção, dentes à mostra em um sorriso cruel. O momento do confronto é iminente.
<h3>Iniciativa:</h3>
{jogador['nome']}: 15 - Goblin: 10
<br><br>
{jogador['nome']}, você age primeiro. O que deseja fazer? """ # noqa E501


def enviar(mensagem, lista_mensagens=[], reiniciar=False):
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
            
            
        
            a ficha do jogador é {jogador}
                lembre-se do torno da criatura se ela ainda estiver viva.
                nivel de dificuldade = alto
                """ # noqa E501
            }
        )
        lista_mensagens.append(
            {"role": "assistant", "content": exemplo})
    if mensagem:
        lista_mensagens.append(
            {"role": "user", "content": mensagem})
    print(lista_mensagens)

    if not reiniciar:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=lista_mensagens,
        )
        # print(response)
        lista_mensagens.append(response["choices"][0]["message"])

    return lista_mensagens


def jogo_adivinhacao(request):

    if request.method == 'GET':
        response = [{'role': 'assistant', 'content': exemplo}]
    elif request.method == 'POST':
        mensagem_atual = request.POST.get('mensagem', '')
        reiniciar = bool(request.POST.get('reiniciar', False))
        response = enviar(mensagem_atual, reiniciar=reiniciar)
        return render(request, 'chat.html', {
            'resposta': response,
            'personagem': jogador})
    return render(request, 'chat.html', {'resposta': response,
                                         'personagem': jogador})
