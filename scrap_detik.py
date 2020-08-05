import requests
from bs4 import BeautifulSoup

html = 'https://www.detik.com/terpopuler'

website = requests.get(html , params={'tag_from': 'wb_cb_mostPopular_more'})

# print(website) # hasilnya status code
# print(website.text) # hasil A

soup = BeautifulSoup(website.text, 'html.parser')

# print(soup) # hasil A

'''
Mencari Atribut dengan .find atau .findAll 
.find = mencari secara spesifik
.findAll = mencari keseluruhan attribut yg sesuai
'''

popular_area = soup.find(attrs={'class':'grid-row list-content'})

# print(popular_area) # hasilnya yg ada di class tsb.

titles = popular_area.findAll(attrs={'class':'media__title'})
images = popular_area.findAll(attrs={'class':'media__image'})
# print(titles) # hasilnya yang ada di class tsb

#for title in titles:
#    print(title.text) #.text tanpa lambang2

for image in images:
    print(image.find('a').find('img')['title'])