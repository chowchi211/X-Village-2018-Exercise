
import json
import requests

url = 'https://cloud.culture.tw/frontsite/trans/SearchShowAction.do?method=doFindTypeJ&category=5'
response = requests.get(url)
print(type(response.text))
    
with open('music_show.json','w', encoding='utf-8-sig') as f:
    f.write(response.text)

with open('music_show.json','r', encoding='utf-8-sig') as g:
  
    show=json.load(g)
    print(type(show))
    print(len(show))
x=''

for i in range(0,len(show)):
    x = x + show[i]['title']+':'+ show[i]['startDate']+'~'+show[i]['endDate']+ '\n'
    print(x)
    
with open('music.txt','w',encoding='utf-8-sig') as h:
    h.write(x)