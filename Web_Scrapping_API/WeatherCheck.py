import requests
from ftplib import FTP

def createWeatheritem(item):
    weatheritem = {}
    weatheritem['currentTemp'] = int(round(item['main']['temp']))
    weatheritem['maxTemp'] = int(round(item['main']['temp_max']))
    weatheritem['minTemp'] = int(round(item['main']['temp_min']))
    weatheritem['condition'] = item['weather'][0]['description']

    return weatheritem

apiKey = ""
country = "au"
city = "Bargo"
currenturl = f"http://api.openweathermap.org/data/2.5/weather?q={city},{country}&units=metric&APPID={apiKey}"
forecasturl = f"http://api.openweathermap.org/data/2.5/forecast?q={city},{country}&cnt=2&units=metric&APPID={apiKey}"


# try:
#     weather = requests.get(currenturl).json()
#     todayWeather = createWeatheritem(weather)
#     print(todayWeather)
# except:
#     "failed to find the request city or country"


weather = requests.get(forecasturl).json()
print(weather)