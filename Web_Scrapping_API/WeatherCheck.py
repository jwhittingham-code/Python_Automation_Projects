import requests
from datetime import date

today = date.today()
currentday = str(today).split("-")[2]

def createWeatheritem(item):
    weatheritem = {}
    weatheritem['currentTemp'] = int(round(item['main']['temp']))
    weatheritem['maxTemp'] = int(round(item['main']['temp_max']))
    weatheritem['minTemp'] = int(round(item['main']['temp_min']))
    weatheritem['condition'] = item['weather'][0]['description']

    return weatheritem

def createforecast(items):
    weatheritem = []
    
    for item in items['list']:
        
        if str(item['dt_txt']).split(" ")[1] == "00:00:00":
            newitem = createWeatheritem(item)
            newitem["date"] = str(item["dt_txt"]).split(" ")[0]
           
            weatheritem.append(newitem)
    
    return weatheritem

apiKey = "-"
country = "au"
city = "Bargo"
currenturl = f"http://api.openweathermap.org/data/2.5/weather?q={city},{country}&units=metric&APPID={apiKey}"
forecasturl = f"http://api.openweathermap.org/data/2.5/forecast?q={city},{country}&units=metric&APPID={apiKey}"

weather = createWeatheritem(requests.get(currenturl).json())
forecast = createforecast(requests.get(forecasturl).json())

print(weather)
print()
print(forecast)
