import csv

pokemon = [
    ['Pikachu', 35, 55, 30, 50, 40, 90],
    ['Charizard', 78, 84, 78, 109, 85, 100],
    ['Magikarp', 20, 10, 55, 15, 20, 80]
]

with open('pokemon.csv', 'w', newline='', encoding='utf-8') as fichier_csv:
    ecrivain_csv = csv.writer(fichier_csv)
    for ligne in pokemon:
        ecrivain_csv.writerow(ligne)


def lecteur(nom_fichier):
    pokemon_stats = {}
    with open('pokemon.csv', 'r', encoding='utf-8') as fichier_csv:
        lecteur_csv = csv.reader(fichier_csv)
        for ligne in lecteur_csv:
            nom_pokemon = ligne[0]
            stats = [int(stat) for stat in ligne[1:]]
            pokemon_stats[nom_pokemon] = stats
    return pokemon_stats


pkmn = lecteur('pokemon.csv')

for nom, stats in pkmn.items():
    print(f'{nom}:{stats}')

print(isinstance(pkmn, dict))
print(isinstance(pkmn['Pikachu'], list))
print(isinstance(pkmn['Pikachu'][0], int))
