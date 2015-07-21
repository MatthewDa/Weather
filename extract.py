import urllib2 as urllib
import json as js
 
def extract_weather(city_country='nyc,usa'):
    city_url = urllib.urlopen('http://api.openweathermap.org/data/2.5/weather?q='+ city_country)
    info_html = city_url.read()
    weather_params = js.loads(info_html)
    temp_K = weather_params['main']['temp']
    temp_F = (temp_K - 273.15) *1.8000 + 32.00
    return int(temp_F)

def catergorize(temp):
    if 61<temp<80:
        return 'The Burrow'
    if 21<temp<30:
        return 'Malfoy Manor'
    if 81<temp<100:
        return 'Shrieking Shack'
    if 31<temp<50:
        return 'Diagon Alley'
    if 51<temp<60:
        return 'Hogwarts'
    if 0<temp<20:
        return 'Azkaban'

def combo(city_country='nyc,usa'):
    print (catergorize(extract_weather(city_country)))
        
       
