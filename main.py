import requests
import json
import time

timer = 1
while timer == 1:
    times = 0
    file = requests.get('https://web.trafi.com/api/additional-transport/vilnius/carsharing')
    car = json.loads(file.text)
    for i in car["cars"]:
        x = i["car"]["plateNumber"]
        y = i["car"]["coordinate"]
        print(x)
        print(y["lat"])
        print(y["lng"])
        times =+ 1
    print("timecount: ", times)
    print("sec: ", times*60)
    time.sleep(60)