print('Penggunaan OOP')
print('Scrap jadwal sholat PKPU')

import requests
from bs4 import BeautifulSoup

#fungsi beautiful soup 4 yaitu memecah struktur teks menjadi elemen kecil.
#fungsi requests yaitu mengambil informasi di suatu url atau website.

url = 'https://jadwalsholat.pkpu.or.id/'
isi = requests.get(url)

if isi.status_code == 200:
    print('\nSuccess!')   # bila hasil 200 maka sukses mengakses -> you can check on web list HTTP error
    print('\nContent', isi.text)
else:
    print('Woops, ada kesalahan requests', isi.status_code)

soup = BeautifulSoup(isi.text, features="html.parser")
print('\nHasil pemanggilan', url)

# karena kita mau judul yang lebih bersih dari lambang2 aneh ketik dengan '.string' di soup.title

print('Title dari url :', soup.title.string)

cari_tablehighlight = soup.find_all('tr','table_highlight')
cari_tablehighlight = (cari_tablehighlight[0])
print(cari_tablehighlight)

sholat ={}
m = 0
for d in cari_tablehighlight:
    if m == 1:
        sholat['Shubuh']= d.get_text()
    elif m == 2:
        sholat['Dzuhur'] = d.get_text()
    elif m == 3:
        sholat['Ashr'] = d.get_text()
    elif m == 4:
        sholat['Maghrib'] = d.get_text()
    elif m == 5:
        sholat['Isya'] = d.get_text()
    m += 1

print(sholat)
print(sholat['Maghrib'])





