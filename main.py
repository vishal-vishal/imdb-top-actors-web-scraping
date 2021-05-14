import requests
import html5lib
from bs4 import BeautifulSoup
import csv

url = "https://www.imdb.com/list/ls050274118/"
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html5lib')

table = soup.find('div',attrs={'class','lister-list'})
top_100_actor = []
for row in table.find_all('div',attrs={'mode-detail'}):
  actor = {}
  actor['image'] = row.find('div',attrs={'class':'lister-item-image'}).a.img['src']
  actor['Rank'] = row.find('span',attrs={'class':'lister-item-index'}).text
  actor['Name'] = row.find('h3',attrs={'class':'lister-item-header'}).text.replace("    ","")[7:].replace("\n","")
  actor['About'] = row.find('p',attrs={'class':None}).text[4:]
  actor['Description'] = row.find('div',attrs={'class':'list-description'}).text.replace("\n",",")
  top_100_actor.append(actor)
  

keys = top_100_actor[0].keys()
# print(key)

with open('actors.csv', 'w', newline='')  as output_file:
    dict_writer = csv.DictWriter(output_file, keys)
    dict_writer.writeheader()
    dict_writer.writerows(top_100_actor) 
