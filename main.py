import requests
import json

file = requests.get('https://web.trafi.com/api/additional-transport/vilnius/carsharing')
car = json.loads(file.text)
for i in car["cars"]:
    x = i["car"]["plateNumber"]
    y = i["car"]["coordinate"]
    print(x)
    print(y["lat"])
    print(y["lng"])