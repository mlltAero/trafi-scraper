import cloudscraper
import json

scraper = cloudscraper.create_scraper()  # returns a CloudScraper instance
# Or: scraper = cloudscraper.CloudScraper()  # CloudScraper inherits from requests.Session
file = scraper.get("https://web.trafi.com/api/map-markers/vilnius/transports?bounds=54.7818886799772%2C25.437952041625977%3B54.58977893569762%2C25.437952041625977%3B54.58977893569762%2C25.13445472717285%3B54.7818886799772%2C25.13445472717285").text  # => "<!DOCTYPE html><html><head>..."
with open('received_file', 'w') as outfile:
    json.dump(file, outfile)

