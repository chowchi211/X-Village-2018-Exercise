import json

with open('train.json',encoding = 'utf-8-sig') as f:
    train = json.load(f)
    print(json.dumps(train, indent=4))
    
