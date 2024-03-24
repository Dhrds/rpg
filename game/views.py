from django.shortcuts import render
import openai
import os
# noqa E501  
openai.api_key = os.getenv("OPENAI_API_KEY")

jogador = {
        "nome": "Elora Galanodel",
        "raca": "Elfa da Lua",
        "classe": {
            "nome": "Ranger",
            "subclasse": "Arqueira Mística"
        },
        "alinhamento": "Neutra e Boa",
        "historico": """
            Filha de um renomado guerreiro élfico e de uma sábia druida,
            Elora sempre se sentiu atraída pela natureza e pela aventura.
            Desde pequena, treinava arco e flecha com seu pai,
            aprendendo a se camuflar na floresta com sua mãe.
            Aos 100 anos, Elora partiu em sua primeira jornada,
            buscando explorar o mundo e ajudar os necessitados.""",
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
                "Bestas de mao",
                "Espadas longas",
                "Espadas curtas"
                ],
            "ferramentas": [
                "Kit de Herbalismo",
                "Kit de Explorador"
                ],
            "pericias": [
                "Intuicao da Natureza",
                "Prestidigitação",
                "Rastrear",
                "Sobrevivencia"
                ]
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
        "caracteristicasClasse": {
            "estiloCombate": "Arquearia",
            "defesaDaNatureza": " +1 em CA quando não estiver usando armadura",
            "favorecidoDosInimigos": "+2 em testes de Percepção para rastrear criaturas favoritas", # noqa E501
            "inimigoPredileto": "+4 em dano contra criaturas favoritas"
            },
        "informacoesAdicionais": {
            "antecedentes": "Forasteiro",
            "lacos": "Irmã mais nova, Lyrissa",
            "ideais": "Proteger a natureza e ajudar os necessitados",
            "personalidade": "Aventureira, gentil, protetora",
            "inspiracao": "Elora se inspira nos ensinamentos de sua mãe sobre a importância da natureza e na bravura de seu pai. Ela busca usar suas habilidades para proteger os fracos e lutar contra a injustiça."} # noqa
    } # noqa E501
exemplo = """Você se encontra nas profundezas de uma caverna sombria,cujas paredes de pedra se estendem pela escuridão como sentinelas antigas. O cheiro de mofo e abandono paira no ar,misturado com o eco distante de goteiras que ressoam pelas galerias vazias. Elora Galanodel, a destemida Elfa da Lua e Arqueira Mística, avança com passos cautelosos, seu instinto aguçado pela presença de perigo iminente. Seu arco longo preparado, uma flecha mágica envolta em energia arcanas pronta para ser disparada. Em meio às sombras dançantes, um rosnado gutural ecoa pela caverna, seguido pelo surgimento furtivo de um goblin. A criatura de pele verde e olhos ardilosos segura uma lança improvisada, pronta para o combate. O goblin avança em sua direção, dentes à mostra em um sorriso cruel. O momento do confronto é iminente. **Iniciativa:** - Elora Galanodel: 15 - Goblin: 10 Elora, você age primeiro. O que deseja fazer? """ # noqa E501


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
        
        Preparem-se para uma jornada épica, onde a coragem e a astúcia serão testadas ao limite.
        Que suas escolhas moldem o destino deste mundo e que suas proezas sejam cantadas por gerações.
        
        EXEMPLO DE INTERAÇÃO COM O USUARIO:
    
        '{exemplo}

        Elora prepara sua flecha mágica e mira com precisão no goblin que avança em sua direção. 
        **Ataque com Arco Longo:** - 
        Rolagem de Ataque: 
        d20 + modificador de Destreza + bônus de Proficiência - Dano da Flecha: 
        1d8 + modificador de Destreza + dano adicional da flecha mágica Vamos fazer a rolagem para o ataque:
        1. Rolagem de Ataque:
        d20 + 3 (modificador de Destreza) + 2 (bônus de Proficiência) Vou fazer a rolagem para você.
        *O dado é lançado e rola para...* 
        Resultado: 17 + 3 (modificador de Destreza) + 2 (bônus de Proficiência) = 
        22 O ataque de Elora acerta em cheio o goblin! Agora vamos calcular o dano:
        2. Dano da Flecha: 1d8 + 3 (modificador de Destreza) Vou rolar o dado de dano para você.
        *O dado é lançado e rola para...* 
        Dano da Flecha: 5 + 3 (modificador de Destreza) = 8 de dano A flecha mágica de Elora perfura o goblin,
        causando 8 pontos de dano.'
      
      
        a ficha do jogador é {jogador}
    
    
                """ # noqa E501
            }
        )
        lista_mensagens.append(
            {"role": "assistant", "content": exemplo})
    lista_mensagens.append(
        {"role": "user", "content": mensagem})
    print(lista_mensagens)

    if not reiniciar:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=lista_mensagens,
        )
        print(response)
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
