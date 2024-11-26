import random as r

meme_dict = {
            "CRINGE": "Algo excepcionalmente raro o embarazoso",
            "LOL": "Una respuesta común a algo gracioso",
            'XD': 'Una respuesta de risa a algo gracioso o divertido',
            'MEWING': 'Habilidad de estirar la mandibula para adelante, se hace mucho para aparecer bien en una foto o para ligar',
            'WTF': 'Asombro de algo extraño o espontaneo',
            'PVP': 'Jugador contra jugador, se hacen muchos en vidojuegos de combate',
            'GIGACHAD': 'Personaje ficticio muy musculoso, lo usan en comparaciones de fuerza',
            'SKIBIDITOILET': 'Personaje ficticio de una serie animada, es un inodoro con una cabeza humana saliendo por la taza',
            'SIGMA': 'Alguien que tiene mewing y confunde a gente diciendole que quiere ligar pero los engaña y se va',
            'TROLLFACE': 'Cara de personaje que hace bromas, hackea o engaña a alguien. Hay muchas variantes',
            'ELPEPE': 'Personaje que es un sapo y se usa para algunos memes'
            }

print(meme_dict.keys())
word = input("Escribe una palabra que no entiendas o escribe sorprendeme: ").upper()
if word in meme_dict.keys():
    print('Esto significa:', meme_dict[word])

elif word == 'SORPRENDEME':
    x = r.choice(list(meme_dict.keys()))
    print('La palabra que conocerás hoy es...' + x + ':' + meme_dict[x])

else:
    print('Esta palabra aun no se incluye en el diccionario, preguntale a tu nieto.')


    
