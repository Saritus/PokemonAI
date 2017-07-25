pokemon = [
    {"Number": 1, "Name": "Bulbasaur", "Type1": "Grass", "Type2": "Poison"},
    {"Number": 2, "Name": "Ivysaur", "Type1": "Grass", "Type2": "Poison"},
    {"Number": 3, "Name": "Venusaur", "Type1": "Grass", "Type2": "Poison"},
    {"Number": 4, "Name": "Charmander", "Type1": "Fire", "Type2": ""},
    {"Number": 5, "Name": "Charmeleon", "Type1": "Fire", "Type2": ""},
    {"Number": 6, "Name": "Charizard", "Type1": "Fire", "Type2": "Flying"},
    {"Number": 7, "Name": "Squirtle", "Type1": "Water", "Type2": ""},
    {"Number": 8, "Name": "Wartortle", "Type1": "Water", "Type2": ""},
    {"Number": 9, "Name": "Blastoise", "Type1": "Water", "Type2": ""},
    {"Number": 10, "Name": "Caterpie", "Type1": "Bug", "Type2": ""},
    {"Number": 11, "Name": "Metapod", "Type1": "Bug", "Type2": ""},
    {"Number": 12, "Name": "Butterfree", "Type1": "Bug", "Type2": "Flying"},
    {"Number": 13, "Name": "Weedle", "Type1": "Bug", "Type2": "Poison"},
    {"Number": 14, "Name": "Kakuna", "Type1": "Bug", "Type2": "Poison"},
    {"Number": 15, "Name": "Beedrill", "Type1": "Bug", "Type2": "Poison"},
    {"Number": 16, "Name": "Pidgey", "Type1": "Normal", "Type2": "Flying"},
    {"Number": 17, "Name": "Pidgeotto", "Type1": "Normal", "Type2": "Flying"},
    {"Number": 18, "Name": "Pidgeot", "Type1": "Normal", "Type2": "Flying"},
    {"Number": 19, "Name": "Rattata", "Type1": "Normal", "Type2": ""},
    {"Number": 20, "Name": "Raticate", "Type1": "Normal", "Type2": ""},
    {"Number": 21, "Name": "Spearow", "Type1": "Normal", "Type2": "Flying"},
    {"Number": 22, "Name": "Fearow", "Type1": "Normal", "Type2": "Flying"},
    {"Number": 23, "Name": "Ekans", "Type1": "Poison", "Type2": ""},
    {"Number": 24, "Name": "Arbok", "Type1": "Poison", "Type2": ""},
    {"Number": 25, "Name": "Pikachu", "Type1": "Electric", "Type2": ""},
    {"Number": 26, "Name": "Raichu", "Type1": "Electric", "Type2": ""},
    {"Number": 27, "Name": "Sandshrew", "Type1": "Ground", "Type2": ""},
    {"Number": 28, "Name": "Sandslash", "Type1": "Ground", "Type2": ""},
    {"Number": 29, "Name": "NidoranW", "Type1": "Poison", "Type2": ""},
    {"Number": 30, "Name": "Nidorina", "Type1": "Poison", "Type2": ""},
    {"Number": 31, "Name": "Nidoqueen", "Type1": "Poison", "Type2": "Ground"},
    {"Number": 32, "Name": "NidoranM", "Type1": "Poison", "Type2": ""},
    {"Number": 33, "Name": "Nidorino", "Type1": "Poison", "Type2": ""},
    {"Number": 34, "Name": "Nidoking", "Type1": "Poison", "Type2": "Ground"},
    {"Number": 35, "Name": "Clefairy", "Type1": "Normal", "Type2": ""},
    {"Number": 36, "Name": "Clefable", "Type1": "Normal", "Type2": ""},
    {"Number": 37, "Name": "Vulpix", "Type1": "Fire", "Type2": ""},
    {"Number": 38, "Name": "Ninetales", "Type1": "Fire", "Type2": ""},
    {"Number": 39, "Name": "Jigglypuff", "Type1": "Normal", "Type2": ""},
    {"Number": 40, "Name": "Wigglytuff", "Type1": "Normal", "Type2": ""},
    {"Number": 41, "Name": "Zubat", "Type1": "Poison", "Type2": "Flying"},
    {"Number": 42, "Name": "Golbat", "Type1": "Poison", "Type2": "Flying"},
    {"Number": 43, "Name": "Oddish", "Type1": "Grass", "Type2": "Poison"},
    {"Number": 44, "Name": "Gloom", "Type1": "Grass", "Type2": "Poison"},
    {"Number": 45, "Name": "Vileplume", "Type1": "Grass", "Type2": "Poison"},
    {"Number": 46, "Name": "Paras", "Type1": "Bug", "Type2": "Grass"},
    {"Number": 47, "Name": "Parasect", "Type1": "Bug", "Type2": "Grass"},
    {"Number": 48, "Name": "Venonat", "Type1": "Bug", "Type2": "Poison"},
    {"Number": 49, "Name": "Venomoth", "Type1": "Bug", "Type2": "Poison"},
    {"Number": 50, "Name": "Diglett", "Type1": "Ground", "Type2": ""},
    {"Number": 51, "Name": "Dugtrio", "Type1": "Ground", "Type2": ""},
    {"Number": 52, "Name": "Meowth", "Type1": "Normal", "Type2": ""},
    {"Number": 53, "Name": "Persian", "Type1": "Normal", "Type2": ""},
    {"Number": 54, "Name": "Psyduck", "Type1": "Water", "Type2": ""},
    {"Number": 55, "Name": "Golduck", "Type1": "Water", "Type2": ""},
    {"Number": 56, "Name": "Mankey", "Type1": "Fighting", "Type2": ""},
    {"Number": 57, "Name": "Primeape", "Type1": "Fighting", "Type2": ""},
    {"Number": 58, "Name": "Growlithe", "Type1": "Fire", "Type2": ""},
    {"Number": 59, "Name": "Arcanine", "Type1": "Fire", "Type2": ""},
    {"Number": 60, "Name": "Poliwag", "Type1": "Water", "Type2": ""},
    {"Number": 61, "Name": "Poliwhirl", "Type1": "Water", "Type2": ""},
    {"Number": 62, "Name": "Poliwrath", "Type1": "Water", "Type2": "Fighting"},
    {"Number": 63, "Name": "Abra", "Type1": "Psychic", "Type2": ""},
    {"Number": 64, "Name": "Kadabra", "Type1": "Psychic", "Type2": ""},
    {"Number": 65, "Name": "Alakazam", "Type1": "Psychic", "Type2": ""},
    {"Number": 66, "Name": "Machop", "Type1": "Fighting", "Type2": ""},
    {"Number": 67, "Name": "Machoke", "Type1": "Fighting", "Type2": ""},
    {"Number": 68, "Name": "Machamp", "Type1": "Fighting", "Type2": ""},
    {"Number": 69, "Name": "Bellsprout", "Type1": "Grass", "Type2": "Poison"},
    {"Number": 70, "Name": "Weepinbell", "Type1": "Grass", "Type2": "Poison"},
    {"Number": 71, "Name": "Victreebel", "Type1": "Grass", "Type2": "Poison"},
    {"Number": 72, "Name": "Tentacool", "Type1": "Water", "Type2": "Poison"},
    {"Number": 73, "Name": "Tentacruel", "Type1": "Water", "Type2": "Poison"},
    {"Number": 74, "Name": "Geodude", "Type1": "Rock", "Type2": "Ground"},
    {"Number": 75, "Name": "Graveler", "Type1": "Rock", "Type2": "Ground"},
    {"Number": 76, "Name": "Golem", "Type1": "Rock", "Type2": "Ground"},
    {"Number": 77, "Name": "Ponyta", "Type1": "Fire", "Type2": ""},
    {"Number": 78, "Name": "Rapidash", "Type1": "Fire", "Type2": ""},
    {"Number": 79, "Name": "Slowpoke", "Type1": "Water", "Type2": "Psychic"},
    {"Number": 80, "Name": "Slowbro", "Type1": "Water", "Type2": "Psychic"},
    {"Number": 81, "Name": "Magnemite", "Type1": "Electric", "Type2": ""},
    {"Number": 82, "Name": "Magneton", "Type1": "Electric", "Type2": ""},
    {"Number": 83, "Name": "Farfetch'd", "Type1": "Normal", "Type2": "Flying"},
    {"Number": 84, "Name": "Doduo", "Type1": "Normal", "Type2": "Flying"},
    {"Number": 85, "Name": "Dodrio", "Type1": "Normal", "Type2": "Flying"},
    {"Number": 86, "Name": "Seel", "Type1": "Water", "Type2": ""},
    {"Number": 87, "Name": "Dewgong", "Type1": "Water", "Type2": "Ice"},
    {"Number": 88, "Name": "Grimer", "Type1": "Poison", "Type2": ""},
    {"Number": 89, "Name": "Muk", "Type1": "Poison", "Type2": ""},
    {"Number": 90, "Name": "Shellder", "Type1": "Water", "Type2": ""},
    {"Number": 91, "Name": "Cloyster", "Type1": "Water", "Type2": "Ice"},
    {"Number": 92, "Name": "Gastly", "Type1": "Ghost", "Type2": "Poison"},
    {"Number": 93, "Name": "Haunter", "Type1": "Ghost", "Type2": "Poison"},
    {"Number": 94, "Name": "Gengar", "Type1": "Ghost", "Type2": "Poison"},
    {"Number": 95, "Name": "Onix", "Type1": "Rock", "Type2": "Ground"},
    {"Number": 96, "Name": "Drowzee", "Type1": "Psychic", "Type2": ""},
    {"Number": 97, "Name": "Hypno", "Type1": "Psychic", "Type2": ""},
    {"Number": 98, "Name": "Krabby", "Type1": "Water", "Type2": ""},
    {"Number": 99, "Name": "Kingler", "Type1": "Water", "Type2": ""},
    {"Number": 100, "Name": "Voltorb", "Type1": "Electric", "Type2": ""},
    {"Number": 101, "Name": "Electrode", "Type1": "Electric", "Type2": ""},
    {"Number": 102, "Name": "Exeggcute", "Type1": "Grass", "Type2": "Psychic"},
    {"Number": 103, "Name": "Exeggutor", "Type1": "Grass", "Type2": "Psychic"},
    {"Number": 104, "Name": "Cubone", "Type1": "Ground", "Type2": ""},
    {"Number": 105, "Name": "Marowak", "Type1": "Ground", "Type2": ""},
    {"Number": 106, "Name": "Hitmonlee", "Type1": "Fighting", "Type2": ""},
    {"Number": 107, "Name": "Hitmonchan", "Type1": "Fighting", "Type2": ""},
    {"Number": 108, "Name": "Lickitung", "Type1": "Normal", "Type2": ""},
    {"Number": 109, "Name": "Koffing", "Type1": "Poison", "Type2": ""},
    {"Number": 110, "Name": "Weezing", "Type1": "Poison", "Type2": ""},
    {"Number": 111, "Name": "Rhyhorn", "Type1": "Ground", "Type2": "Rock"},
    {"Number": 112, "Name": "Rhydon", "Type1": "Ground", "Type2": "Rock"},
    {"Number": 113, "Name": "Chansey", "Type1": "Normal", "Type2": ""},
    {"Number": 114, "Name": "Tangela", "Type1": "Grass", "Type2": ""},
    {"Number": 115, "Name": "Kangaskhan", "Type1": "Normal", "Type2": ""},
    {"Number": 116, "Name": "Horsea", "Type1": "Water", "Type2": ""},
    {"Number": 117, "Name": "Seadra", "Type1": "Water", "Type2": ""},
    {"Number": 118, "Name": "Goldeen", "Type1": "Water", "Type2": ""},
    {"Number": 119, "Name": "Seaking", "Type1": "Water", "Type2": ""},
    {"Number": 120, "Name": "Staryu", "Type1": "Water", "Type2": ""},
    {"Number": 121, "Name": "Starmie", "Type1": "Water", "Type2": "Psychic"},
    {"Number": 122, "Name": "Mr.Mime", "Type1": "Psychic", "Type2": ""},
    {"Number": 123, "Name": "Scyther", "Type1": "Bug", "Type2": "Flying"},
    {"Number": 124, "Name": "Jynx", "Type1": "Ice", "Type2": "Psychic"},
    {"Number": 125, "Name": "Electabuzz", "Type1": "Electric", "Type2": ""},
    {"Number": 126, "Name": "Magmar", "Type1": "Fire", "Type2": ""},
    {"Number": 127, "Name": "Pinsir", "Type1": "Bug", "Type2": ""},
    {"Number": 128, "Name": "Tauros", "Type1": "Normal", "Type2": ""},
    {"Number": 129, "Name": "Magikarp", "Type1": "Water", "Type2": ""},
    {"Number": 130, "Name": "Gyarados", "Type1": "Water", "Type2": "Flying"},
    {"Number": 131, "Name": "Lapras", "Type1": "Water", "Type2": "Ice"},
    {"Number": 132, "Name": "Ditto", "Type1": "Normal", "Type2": ""},
    {"Number": 133, "Name": "Eevee", "Type1": "Normal", "Type2": ""},
    {"Number": 134, "Name": "Vaporeon", "Type1": "Water", "Type2": ""},
    {"Number": 135, "Name": "Jolteon", "Type1": "Electric", "Type2": ""},
    {"Number": 136, "Name": "Flareon", "Type1": "Fire", "Type2": ""},
    {"Number": 137, "Name": "Porygon", "Type1": "Normal", "Type2": ""},
    {"Number": 138, "Name": "Omanyte", "Type1": "Rock", "Type2": "Water"},
    {"Number": 139, "Name": "Omastar", "Type1": "Rock", "Type2": "Water"},
    {"Number": 140, "Name": "Kabuto", "Type1": "Rock", "Type2": "Water"},
    {"Number": 141, "Name": "Kabutops", "Type1": "Rock", "Type2": "Water"},
    {"Number": 142, "Name": "Aerodactyl", "Type1": "Rock", "Type2": "Flying"},
    {"Number": 143, "Name": "Snorlax", "Type1": "Normal", "Type2": ""},
    {"Number": 144, "Name": "Articuno", "Type1": "Ice", "Type2": "Flying"},
    {"Number": 145, "Name": "Zapdos", "Type1": "Electric", "Type2": "Flying"},
    {"Number": 146, "Name": "Moltres", "Type1": "Fire", "Type2": "Flying"},
    {"Number": 147, "Name": "Dratini", "Type1": "Dragon", "Type2": ""},
    {"Number": 148, "Name": "Dragonair", "Type1": "Dragon", "Type2": ""},
    {"Number": 149, "Name": "Dragonite", "Type1": "Dragon", "Type2": "Flying"},
    {"Number": 150, "Name": "Mewtwo", "Type1": "Psychic", "Type2": ""},
    {"Number": 151, "Name": "Mew", "Type1": "Psychic", "Type2": ""}
]

type_multiplicator = {
    "Normal": {"Normal": 1, "Fire": 1, "Water": 1, "Electric": 1, "Grass": 1, "Ice": 1, "Fighting": 1, "Poison": 1, "Ground": 1, "Flying": 1,
               "Psychic": 1, "Bug": 1, "Rock": 0.5, "Ghost": 0, "Dragon": 1},
    "Fire": {"Normal": 1, "Fire": 0.5, "Water": 0.5, "Electric": 1, "Grass": 2, "Ice": 2, "Fighting": 1, "Poison": 1, "Ground": 1, "Flying": 1,
             "Psychic": 1, "Bug": 2, "Rock": 0.5, "Ghost": 1, "Dragon": 0.5},
    "Water": {"Normal": 1, "Fire": 2, "Water": 0.5, "Electric": 1, "Grass": 0.5, "Ice": 1, "Fighting": 1, "Poison": 1, "Ground": 2, "Flying": 1,
              "Psychic": 1, "Bug": 1, "Rock": 2, "Ghost": 1, "Dragon": 0.5},
    "Electric": {"Normal": 1, "Fire": 1, "Water": 2, "Electric": 0.5, "Grass": 0.5, "Ice": 1, "Fighting": 1, "Poison": 1, "Ground": 0, "Flying": 2,
                 "Psychic": 1, "Bug": 1, "Rock": 1, "Ghost": 1, "Dragon": 0.5},
    "Grass": {"Normal": 1, "Fire": 0.5, "Water": 2, "Electric": 1, "Grass": 0.5, "Ice": 1, "Fighting": 1, "Poison": 0.5, "Ground": 2, "Flying": 0.5,
              "Psychic": 1, "Bug": 0.5, "Rock": 2, "Ghost": 1, "Dragon": 0.5},
    "Ice": {"Normal": 1, "Fire": 0.5, "Water": 0.5, "Electric": 1, "Grass": 2, "Ice": 0.5, "Fighting": 1, "Poison": 1, "Ground": 2, "Flying": 2,
            "Psychic": 1, "Bug": 1, "Rock": 1, "Ghost": 1, "Dragon": 2},
    "Fighting": {"Normal": 2, "Fire": 1, "Water": 1, "Electric": 1, "Grass": 1, "Ice": 2, "Fighting": 1, "Poison": 0.5, "Ground": 1, "Flying": 0.5,
                 "Psychic": 0.5, "Bug": 0.5, "Rock": 2, "Ghost": 0, "Dragon": 1},
    "Poison": {"Normal": 1, "Fire": 1, "Water": 1, "Electric": 1, "Grass": 2, "Ice": 1, "Fighting": 1, "Poison": 0.5, "Ground": 0.5, "Flying": 1,
               "Psychic": 1, "Bug": 1, "Rock": 0.5, "Ghost": 0.5, "Dragon": 1},
    "Ground": {"Normal": 1, "Fire": 2, "Water": 1, "Electric": 2, "Grass": 0.5, "Ice": 1, "Fighting": 1, "Poison": 2, "Ground": 1, "Flying": 0,
               "Psychic": 1, "Bug": 0.5, "Rock": 2, "Ghost": 1, "Dragon": 1},
    "Flying": {"Normal": 1, "Fire": 1, "Water": 1, "Electric": 0.5, "Grass": 2, "Ice": 1, "Fighting": 2, "Poison": 1, "Ground": 1, "Flying": 1,
               "Psychic": 1, "Bug": 2, "Rock": 0.5, "Ghost": 1, "Dragon": 1},
    "Psychic": {"Normal": 1, "Fire": 1, "Water": 1, "Electric": 1, "Grass": 1, "Ice": 1, "Fighting": 2, "Poison": 2, "Ground": 1, "Flying": 1,
                "Psychic": 0.5, "Bug": 1, "Rock": 1, "Ghost": 1, "Dragon": 1},
    "Bug": {"Normal": 1, "Fire": 0.5, "Water": 1, "Electric": 1, "Grass": 2, "Ice": 1, "Fighting": 0.5, "Poison": 0.5, "Ground": 1, "Flying": 0.5,
            "Psychic": 2, "Bug": 1, "Rock": 1, "Ghost": 0.5, "Dragon": 1},
    "Rock": {"Normal": 1, "Fire": 2, "Water": 1, "Electric": 1, "Grass": 1, "Ice": 2, "Fighting": 0.5, "Poison": 1, "Ground": 0.5, "Flying": 2,
             "Psychic": 1, "Bug": 2, "Rock": 1, "Ghost": 1, "Dragon": 1},
    "Ghost": {"Normal": 0, "Fire": 1, "Water": 1, "Electric": 1, "Grass": 1, "Ice": 1, "Fighting": 1, "Poison": 1, "Ground": 1, "Flying": 1,
              "Psychic": 0, "Bug": 1, "Rock": 1, "Ghost": 2, "Dragon": 1},
    "Dragon": {"Normal": 1, "Fire": 1, "Water": 1, "Electric": 1, "Grass": 1, "Ice": 1, "Fighting": 1, "Poison": 1, "Ground": 1, "Flying": 1,
               "Psychic": 1, "Bug": 1, "Rock": 1, "Ghost": 1, "Dragon": 2}
}


def get_pokemon(index):
    return pokemon[index - 1]


def get_type_multiplicator(attack, defense):
    return type_multiplicator[attack][defense]


def main():
    return


if __name__ == "__main__":
    main()
