import requests
import json
# API Application Programming Interface
# the sending and receiving of json data
# in any language we can make requests to an api
# the api directs those requests and either sends info to a database
# send its back to the client

# syntax of json data 

{
    "name": "Pikachu",
    "type": "Electric",
    "level": 25
}

# json supports a variety of different types
# its up to python to interpret those types 
# by deserializing the json data.

# {
#     "pokemon": "Charmander",
#     "type": "Fire",
#     "level": 15,
#     "isEvolved": false,
#     "evolutionLevel": null

# }

# making a get request to the pokeapi
# makes a GET request to the pokemon api
# which retrieves data and gives us access to a data object that we need to make readable to python
response = requests.get('https://pokeapi.co/api/v2/pokemon/heracross')

data = response.json() #makes the request data readable as a python dictionary

# print(data)
print(data['abilities'])
print(data['name'])
print(data["weight"]) 
for key in data.keys():
    print(key)
print(data['base_experience'])

pokemon = {
    "name": "Pikachu",
    "type": "Electric",
    "level": 25
}

print(pokemon['name'])

print(type(data))

response = requests.get('https://pokeapi.co/api/v2/pokemon/charmander')
json_data = response.text # converts the data from the request to text
# print(json_data)
# Converting JSON to a python dictionary
pokemon_data = json.loads(json_data)

# accessing the data like we do from any python dictionary
print(pokemon_data['name'])
print(pokemon_data['types'])


# try to post to the pokeapi
attempt = requests.post('https://pokeapi.co/api/v2/pokemon/charmander', json = {"color": "blue"})
print(attempt)

# turning a python dictionary into json
# any time we need to post something, we need to translate from python to json so it can be read through the request
pokemon_data = {
    "name": "bulbasaur",
    "type": "Grass",
    "abilities": ["Overgrow", "Chlorophyll"]
}
# converting to JSON - dumping our python dictionary into JSON
json_output = json.dumps(pokemon_data)
print(json_output)
print(type(json_output))

