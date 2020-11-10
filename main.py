import requests
import json
import time

timer = 1
data = open('itm.txt',"w+")
while timer == 1:
    file = requests.get('https://web.trafi.com/api/additional-transport/vilnius/carsharing')
    car = json.loads(file.text)
    for i in car["cars"]:
        x = i["car"]["plateNumber"]
        y = i["car"]["coordinate"]
        print(x)
        print(y["lat"])
        print(y["lng"])
        data.write(str(x) + "\n")
        data.write(str(y["lat"]) + "\n")
        data.write(str(y["lng"]) + "\n")
    time.sleep(60)