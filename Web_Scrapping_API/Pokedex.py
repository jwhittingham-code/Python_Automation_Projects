import requests, json

baseUrl = 'https://pokeapi.co/api/v2/'

def pickPokemon():
    nameOrId = input("pick a Pokemon by name or ID: ")
    call = requests.get(f'{baseUrl}/pokemon/{nameOrId}')
    #print(call)
    try:
        pokemon = call.json()
        if pokemon:
            return pokemon 
        else:
            return "Failed to find Pokemon"
    except:
        return "Failed to call Pokemon API"

def types(pokemon):
    typesfile = pokemon["types"]
    types = list()
   
    for item in typesfile:
        typeitem = item["type"]
        types.append(typeitem["name"])
    return types

def displayPokemon(pokemon):
    try:
        print('Name: ',pokemon['name'].upper())
        print('ID: ', pokemon['id'])
        typing = ', '.join(types(pokemon))
        print("Types: ",typing)       
    except:
        print("failed")

critter = pickPokemon()
displayPokemon(critter)

