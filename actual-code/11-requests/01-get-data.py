import requests
import csv

"""
METHOD   - GET, POST, DELETE, PATCH, PUT
URL      - https:// http:// chrome:// ftp:// 
HEADERS  - key:value 
PARAMS   - 

https://newsapi.org/v2/everything?q=animals&from=2025-07-28&sortBy=publishedAt&apiKey=9ec9a0b6703b490a86e6715f90185450
"""
API_KEY = "9ec9a0b6703b490a86e6715f90185450" 
query = input("What do you want to have headlines about? ")
url = f"https://newsapi.org/v2/everything?q={query}&from=2025-07-28&sortBy=publishedAt&apiKey={API_KEY}"

response = requests.get(url)
data = response.json()
articles = data["articles"]

# source, author, title, description, url, urlToImage, publishedAt, content

with open("articles.csv", "a") as file:
  writer = csv.writer(file)
  writer.writerow(["source", "author", "title", "description", "url", "urlToImage", "publishedAt", "content"])
  for article in articles:
    writer.writerow([article["source"]["name"], 
                     article["author"], 
                     article["title"].strip(), 
                     article["description"].strip(), 
                     article["url"], 
                     article["urlToImage"], 
                     article["publishedAt"], 
                     article["content"].strip()])