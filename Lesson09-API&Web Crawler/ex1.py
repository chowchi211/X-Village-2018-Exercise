import json
import requests
apikeys='location/2306179/'
url='https://www.metaweather.com/api/'+ apikeys

response=requests.get(url)
# print(type(response.text))

with open ('weather.json', 'w') as f:
    f.write(response.text)

with open ('weather.json', 'r') as g:
    show = json.load(g)
    # print(type(show))
    

print('Today\'s weather is:')
print('='*50 )

for i in show['consolidated_weather']:
    
    
    print('WeatherType:', i['weather_state_name']) 
    print('UploadTime:', i['created'])
    print('temp:', i['the_temp']) 
    
    print('='*50 )
