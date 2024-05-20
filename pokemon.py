import requests
import json
def poke_api_call(pokemon):
    response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon}") 
    json_data = response.text #this is going to store the JSON data to a variable
    poke_data = json.loads(json_data) # converts the JSON data into a python dictionary
    # taking a dictionary that lives as a string 
    # and helping it realize its true form in python
    # poke_data is a dictionary

    print(f"Here is some cool info about {pokemon.title()}")
    print("Their abilities are: ")
    for ability in poke_data['abilities']:
        print(ability['ability']['name'])

    print(f"{pokemon.title()} weighs {poke_data['weight']} pounds?")

    # Print out information about the pokemon's types
    for type in poke_data["types"]:
        print(type['type']['name'])
    # just the names of the types

    # print out the name of the first move in the moves list

    print(poke_data['moves'][0]['move']['name'])

    for i in range(len(poke_data['moves'])):
        print(poke_data["moves"][i]['move']['name'])
        if i == 0:
            break

    

poke_api_call("charmander")




pokemon_dictionary = {
    "name": "Pikachu",
    "type": "Electric",
    "moves": [{"name":"Thunderbolt" }, {"name": "tackle"}]
}

# print(pokemon_dictionary['moves'])
# for move in pokemon_dictionary['moves']:
#     print(move)

# for move in pokemon_dictionary['moves']:
# #     print(move['name'])

# for key, value in pokemon_dictionary.items():
#     print(key, value)





