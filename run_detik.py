import requests
from bs4 import BeautifulSoup
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/detikterpopuler')
def detik_terpopuler():
    html = 'https://www.detik.com/terpopuler'
    website = requests.get(html, params={'tag_from': 'wb_cb_mostPopular_more'})
    soup = BeautifulSoup(website.text, 'html.parser')
    popular_area = soup.find(attrs={'class': 'grid-row list-content'})
    titles = popular_area.findAll(attrs={'class': 'media__title'})
    images = popular_area.findAll(attrs={'class': 'media__image'})
    return render_template('index.html', images = images)

if __name__ == '__main__':
    app.run(debug=True)