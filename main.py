import requests
import json

file = requests.get('https://web.trafi.com/api/additional-transport/vilnius/carsharing').json()
print(file["cars"][0]["car"]["plateNumber"])
print(file["cars"][0]["car"]["coordinate"])
