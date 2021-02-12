import requests as rq
import time as ti
import csv

carsLastPosition = dict()
i = 0

with open('file.csv', mode='w+') as csv_file:
    csvFile = csv.DictWriter(csv_file, fieldnames=['carNum', 'lat', 'lng', 'prevLat', 'prevLng', 'timesMoved'])
    while i != 6:
        ParsedData = (rq.get('https://web.trafi.com/api/additional-transport/vilnius/carsharing').json())["cars"]
        for carData in ParsedData:
            plateNum = carData["car"]["plateNumber"]
            lat = carData["car"]["coordinate"]["lat"]
            lng = carData["car"]["coordinate"]["lng"]
            if plateNum in carsLastPosition:
                locPair = carsLastPosition[plateNum]["loc"] # "loc" as in location
                lastLat = locPair[0]
                lastLng = locPair[1]

                if lat != lastLat or lng != lastLng:
                    carsLastPosition[plateNum]["timesMove"] += 1
                    carsLastPosition[plateNum]["loc"] = [lat, lng]
                    print("Car with plate number " + plateNum + " has moved " + str(carsLastPosition[plateNum]["timesMove"]) + " times.")
                    csvFile.writerow({'carNum': plateNum, 'lat': lat, 'lng': lng, 'prevLat': lastLat, 'prevLng': lastLng, 'timesMoved': carsLastPosition[plateNum]["timesMove"]})

            else:
                carsLastPosition[plateNum] = dict()
                carsLastPosition[plateNum]["loc"] = [lat, lng]
                carsLastPosition[plateNum]["timesMove"] = 0
        i += 1
        ti.sleep(10)