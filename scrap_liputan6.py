import requests, pandas
from bs4 import BeautifulSoup

url = 'https://www.liputan6.com/'
html = requests.get(url)

# print(html.text)

soup = BeautifulSoup(html.text,'html.parser')

# print(soup)

content = soup.find(attrs={'class': 'container clearfix'})

# print(info)

headline = content.findAll(attrs={'class': 'headline--main__title'})
isi = content.findAll(attrs={'class': 'articles--iridescent-list--text-item__title-link-text'})

# print(titles)

for title in headline:
    print(title.text)
for d in isi:
    print(d.text)