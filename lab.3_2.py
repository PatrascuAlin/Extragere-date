
import urllib.request as urllib2
from bs4 import BeautifulSoup
import csv
from datetime import datetime

quote_pages = ['https://www.bman.ro/products/pantaloni-gri-bman428',
               'https://www.bman.ro/products/pantaloni-albi-barbati-bman350']

produse = []

for page in quote_pages:

    page = urllib2.urlopen(page)
    soup = BeautifulSoup(page, 'html.parser')

# extragere pret si nume produsului selectat
    pret = soup.find('div' , attrs={'class': 'single-product-content__price-box__price'})
    pret = pret.text.strip()
    
    nume = soup.find('div' , attrs={'class': 'container'})
    nume = nume.text.strip()

    produse.append((pret, nume))

#adaugare informatii in fisier
with open('bman_pantaloni.csv', 'a') as csv_file:
    writer = csv.writer(csv_file)

    for pret, nume in produse:
        writer.writerow([pret, nume, datetime.now()])
