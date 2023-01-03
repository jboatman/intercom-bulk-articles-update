import requests
import json
import numpy as np
import configparser

config = configparser.ConfigParser()
config.read('config.ini')
token = config['Auth']['token']

articles = []

getUrl = "https://api.intercom.io/articles"
data = {}
headers = {"Content-type": "application/json","Authorization": "Bearer " + token}

data = requests.get(getUrl, data=data, headers=headers).json()

# this can be manually set for testing. Would just set to 1 page to only process the first page.
#pages = 1
pages = data["pages"]["total_pages"]
#articles = array

for x in range(1, pages + 1):
  # fetch each page
  getUrl = f"https://api.intercom.io/articles?page={x}" 
  data = {}
  data = requests.get(getUrl, data=data, headers=headers).json()
  
  data = json.dumps(data)
  json_data = json.loads(data)
  
  #loop through each article in page
  for key in json_data["data"]:
    # build articles array with article ids
    articles.append(key["id"])
    
# save article IDs to CSV
a = np.asarray(articles)
np.savetxt("articles.csv", a, fmt='%s', delimiter=",")


