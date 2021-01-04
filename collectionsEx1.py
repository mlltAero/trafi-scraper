import time
import requests
carsLastPosition = dict()
i = 0
while i != 60:
    data1 = requests.get('https://web.trafi.com/api/additional-transport/vilnius/carsharing').json()
    data = data1["cars"]
    for carData in data:
        plateNumber = carData["car"]["plateNumber"]
        lat = carData["car"]["coordinate"]["lat"]
        lng = carData["car"]["coordinate"]["lng"]

        if plateNumber in carsLastPosition:
            coordinatesPair = carsLastPosition[plateNumber]["coords"]
            lastLat = coordinatesPair[0]
            lastLng = coordinatesPair[1]

            if lat != lastLat or lng != lastLng:
                carsLastPosition[plateNumber]["timesMove"] += 1
                carsLastPosition[plateNumber]["coords"] = [lat, lng]
        else:
            carsLastPosition[plateNumber] = dict()
            carsLastPosition[plateNumber]["coords"] = [lat, lng]
            carsLastPosition[plateNumber]["timesMove"] = 0
    for plateNumber in carsLastPosition:
        if carsLastPosition[plateNumber]["timesMove"] != 0:
            print("Car with plate number " + plateNumber + " has moved " + str(carsLastPosition[plateNumber]["timesMove"]) + " times.")
    time.sleep(30)
    i += 1
file = open("C:\\stuff\\main.txt", "w+", encoding="utf-16")
for plateNumber in carsLastPosition:
    file.write("Car with plate number " + plateNumber + " has moved " + str(carsLastPosition[plateNumber]["timesMove"]) + " times.\n")