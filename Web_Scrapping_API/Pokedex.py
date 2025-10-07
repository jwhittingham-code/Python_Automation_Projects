import requests, json

baseUrl = 'https://pokeapi.co/api/v2/'
name = 'pokemon/ditto'

data = requests.get(f'{baseUrl}{name}')
file = data.json()
print(file)
