import requests
from datetime import date

today = date.today()
currentday = str(today).split("-")[2]
apiKey = "-"
country = "au"
city = "Penrith"
currenturl = f"http://api.openweathermap.org/data/2.5/weather?q={city},{country}&units=metric&APPID={apiKey}"
forecasturl = f"http://api.openweathermap.org/data/2.5/forecast?q={city},{country}&units=metric&APPID={apiKey}"

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

def displayweather(item):
    try:
        dateitem = item["date"]
        current = False
    except:
        dateitem = today
        current = True
    print(city.upper(), " ", dateitem)
    if current:
        print("Current temperature: ", item['currentTemp'])
        print("Current Conditions: ", item['condition'])
    else:
        print("Conditions: ", item['condition'])
    print("Minium temperature: ", item["minTemp"], "    ", "Maximum temperature: ", item["maxTemp"])
    print("---------------------------------------------------------")
    print('')



weather = createWeatheritem(requests.get(currenturl).json())
forecast = createforecast(requests.get(forecasturl).json())

print("---------------------------------------------------------")
print("------------------------Today----------------------------")
print("---------------------------------------------------------")
print()
displayweather(weather)
print("------------------------forecast-------------------------")
print("---------------------------------------------------------")

for item in forecast:
    displayweather(item)
