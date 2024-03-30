
from game.models import Personagem


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
        }
ficha2 = {
    "nome": "Eldarin",
    "raca": "Elfo da Floresta",
    "classe": {
        "nome": "Guerreiro",
        "subclasse": "Campeão"
    },
    "atributos": {
        "forca": 16,
        "modificadorForca": 3,
        "destreza": 14,
        "modificadorDestreza": 2,
        "constituicao": 15,
        "modificadorConstituicao": 2,
        "inteligencia": 10,
        "modificadorInteligencia": 0,
        "sabedoria": 12,
        "modificadorSabedoria": 1,
        "carisma": 10,
        "modificadorCarisma": 0
    },
    "proficiencias": {
        "habilidades": [
            "Atletismo",
            "Percepção",
            "Intimidação",
        ],
        "armas": [
            "Espada longa",
            "Arco longo"
        ],
    },
    "equipamentos": [
        "Espada longa",
        "Armadura de couro",
        "Escudo",
        "Aljava com 20 flechas",
        "Roupas de viajante",
        "10 moedas de ouro",
        "50 moedas de prata"
    ],
}

# Ficha de personagem 3
ficha3 = {
    "nome": "Lilith",
    "raca": "Humana",
    "classe": {
        "nome": "Feiticeira",
        "subclasse": "Invocadora"
    },
    "atributos": {
        "forca": 10,
        "modificadorForca": 0,
        "destreza": 14,
        "modificadorDestreza": 2,
        "constituicao": 12,
        "modificadorConstituicao": 1,
        "inteligencia": 16,
        "modificadorInteligencia": 3,
        "sabedoria": 10,
        "modificadorSabedoria": 0,
        "carisma": 18,
        "modificadorCarisma": 4
    },
    "proficiencias": {
        "habilidades": [
            "Arcana",
            "Enganação",
            "Persuasão"
        ],
        "armas": [
            "Adagas"
        ],
    },
    "equipamentos": [
        "Adagas",
        "Roupas finas",
        "Aljava vazia",
        "10 moedas de ouro",
        "50 moedas de prata"
    ],
    "magicas": {
        "primeiroNivel": [
            "Bola de Fogo",
            "Mísseis Mágicos",
            "Raio de Gelo",
            "Toque do Chocante"
        ]
    },
}
personagem = Personagem(nome=jogador['nome'], ficha=ficha2)
personagem.save()
personagem = Personagem(nome=jogador['nome'], ficha=ficha3)
personagem.save()
personagem = Personagem(nome=jogador['nome'], ficha=jogador)
personagem.save()
