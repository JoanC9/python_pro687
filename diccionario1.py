# Realizado por Esteban Acuña
meme_dict = {
"CRINGE": "Algo excepcionalmente raro o embarazoso",
"LOL": "Una respuesta común a algo gracioso",
"CREEPY": "Algo o alguien atterrador o sieniestro",
"OMG": "Una respuesta que expresa sorpresa o impacto",
"AGGRO": "Es que alguien se ponga furioso o agresivo"
}

for i in range(5):
word = input("Escribe una palabra que no entiendas (¡con mayúsculas!): ")

if word in meme_dict.keys():
print("Esa palabra significa:", meme_dict[word])
else:
print("Esa palabras no se encuentra en el diccionario😔")
