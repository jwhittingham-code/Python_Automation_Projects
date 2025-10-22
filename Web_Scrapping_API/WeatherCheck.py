import requests
from ftplib import FTP

apiKey = ""
country = "au"
city = "Penrith"

baseURL = f"http://api.openweathermap.org/data/2.5/weather?q={city},{country}&units=metric&APPID={apiKey}"

weather = requests.get(baseURL).json()

print(weather)