import requests
import json
import csv
import configparser

config = configparser.ConfigParser()
config.read('config.ini')
token = config['Auth']['token']

filename = 'articles.csv'
headers = {"Content-type": "application/json","Authorization": "Bearer " + token}

results = []
# open csv, read, and generate arr
with open("articles.csv") as csvfile:
    reader = csv.reader(csvfile)
    for row in reader: # each row is a list
        results.append(row)

# for each article in arr. Range used to limit for testing.
for x in results:
  # get article ID and set api url
  articleId = ', '.join(results[x])
  articleUrl = f"https://api.intercom.io/articles/{articleId}"
  
  data = {}
  # get article
  article = requests.get(articleUrl, data=data, headers=headers)

  article = article.json()

  articleBody = article["body"]
  articleTitle = article["title"]
  articleDesc = article["description"]
  
  # replace text
  articleBody = articleBody.replace("Zingle", "Concierge")
  articleTitle = articleTitle.replace("Zingle", "Concierge")
  articleDesc = articleDesc.replace("Zingle", "Concierge")

  # for testing, may want to reverse the replace
  #articleBody = articleBody.replace("Concierge", "Zingle")
  #articleTitle = articleTitle.replace("Concierge", "Zingle")
  #articleDesc = articleDesc.replace("Concierge", "Zingle")

  articleBody = json.dumps(articleBody)
  # create payload with updated title, desc, and body
  putPayload = '{"title":"'+articleTitle+'","description":"'+articleDesc+'","body":'+articleBody+'}'

  # make PUT call with updated payload
  response = requests.put(articleUrl, data=putPayload, headers=headers)
  print(response.content)