from bs4 import BeautifulSoup
from time import sleep
import csv, requests, re, ftfy

# This script provides an example of scraping toponymic data for Chile from tutiempo.net

chile_csv = csv.writer(open('chile-toponyms.csv', 'w', newline=''))
chile_csv.writerow(['Name', 'Description', 'Latitude', 'Longitude', 'Department', 'Type'])

# Administrative Regions

pages = []

pages.append("https://tierra.tutiempo.net/regiones-administrativas/chile/ci.htm")

for item in pages:
    page = requests.get(item)
    soup = BeautifulSoup(page.text, 'html.parser')

    div = soup.find(class_="mlistados paises")
    
    for i in div.find_all('a'):
        for sib in i.next_siblings:
            placename = i.contents[0].encode('latin1').decode('utf-8')
            if sib.name == 'span':
                temp = sib.text.encode('latin1').decode('utf-8')
                fields = temp.split('|')
                chile_csv.writerow([ftfy.fix_text(placename), ftfy.fix_text(fields[0]), ftfy.fix_text(fields[1]), ftfy.fix_text(fields[2]), ftfy.fix_text(fields[3]), "Administrative Region"])
            elif sib.name == 'ul':
                break

# # Hydrology

pages = []

pages.append("https://tierra.tutiempo.net/hidrografia/chile/ci.htm")

for i in range(2, 131):
    url = 'https://tierra.tutiempo.net/hidrografia/chile/ci_' + str(i) + '.htm'
    pages.append(url)

b = 1

for item in pages:
    page = requests.get(item)
    soup = BeautifulSoup(page.text, 'html.parser')

    div = soup.find(class_="mlistados paises")
    
    for i in div.find_all('a'):
        for sib in i.next_siblings:
            placename = i.contents[0].encode('latin1').decode('utf-8')
            if sib.name == 'span':
                temp = sib.text.encode('latin1').decode('utf-8')
                fields = temp.split('|')
                chile_csv.writerow([ftfy.fix_text(placename), ftfy.fix_text(fields[0]), ftfy.fix_text(fields[1]), ftfy.fix_text(fields[2]), ftfy.fix_text(fields[3]), "Hydrology"])
            elif sib.name == 'ul':
                break

    if b == 50 or b == 100 or b == 150:
        sleep(10)

sleep(10)

# # Points of Interest

pages = []

pages.append("https://tierra.tutiempo.net/puntos-caracteristicos/chile/ci.htm")

for i in range(2, 65):
    url = 'https://tierra.tutiempo.net/puntos-caracteristicos/chile/ci_' + str(i) + '.htm'
    pages.append(url)

b = 1

for item in pages:
    page = requests.get(item)
    soup = BeautifulSoup(page.text, 'html.parser')

    div = soup.find(class_="mlistados paises")
    
    for i in div.find_all('a'):
        for sib in i.next_siblings:
            placename = i.contents[0].encode('latin1').decode('utf-8')
            if sib.name == 'span':
                temp = sib.text.encode('latin1').decode('utf-8')
                fields = temp.split('|')
                chile_csv.writerow([ftfy.fix_text(placename), ftfy.fix_text(fields[0]), ftfy.fix_text(fields[1]), ftfy.fix_text(fields[2]), ftfy.fix_text(fields[3]), "Point of Interest"])
            elif sib.name == 'ul':
                break

    if b == 50 or b == 100 or b == 150:
        sleep(10)

sleep(10)

# # Populated Places

pages = []

pages.append("https://tierra.tutiempo.net/lugares-poblados/chile/ci.htm")

for i in range(2, 48):
    url = 'https://tierra.tutiempo.net/lugares-poblados/chile/ci_' + str(i) + '.htm'
    pages.append(url)

for item in pages:
    page = requests.get(item)
    soup = BeautifulSoup(page.text, 'html.parser')

    div = soup.find(class_="mlistados paises")
    
    for i in div.find_all('a'):
        for sib in i.next_siblings:
            placename = i.contents[0].encode('latin1').decode('utf-8')
            if sib.name == 'span':
                temp = sib.text.encode('latin1').decode('utf-8')
                fields = temp.split('|')
                chile_csv.writerow([ftfy.fix_text(placename), ftfy.fix_text(fields[0]), ftfy.fix_text(fields[1]), ftfy.fix_text(fields[2]), ftfy.fix_text(fields[3]), "Populated Place"])
            elif sib.name == 'ul':
                break

# # Places or Areas

pages = []

pages.append("https://tierra.tutiempo.net/lugares-areas/chile/ci.htm")

for i in range(2, 19):
    url = 'https://tierra.tutiempo.net/lugares-areas/chile/ci_' + str(i) + '.htm'
    pages.append(url)

for item in pages:
    page = requests.get(item)
    soup = BeautifulSoup(page.text, 'html.parser')

    div = soup.find(class_="mlistados paises")
    
    for i in div.find_all('a'):
        for sib in i.next_siblings:
            placename = i.contents[0].encode('latin1').decode('utf-8')
            if sib.name == 'span':
                temp = sib.text.encode('latin1').decode('utf-8')
                fields = temp.split('|')
                chile_csv.writerow([ftfy.fix_text(placename), ftfy.fix_text(fields[0]), ftfy.fix_text(fields[1]), ftfy.fix_text(fields[2]), ftfy.fix_text(fields[3]), "Places or Areas"])
            elif sib.name == 'ul':
                break


# # Orography

pages = []

pages.append("https://tierra.tutiempo.net/orografia/chile/ci.htm")

for i in range(2, 166):
    url = 'https://tierra.tutiempo.net/orografia/chile/ci_' + str(i) + '.htm'
    pages.append(url)

b=1

for item in pages:
    page = requests.get(item)
    soup = BeautifulSoup(page.text, 'html.parser')

    div = soup.find(class_="mlistados paises")
    
    for i in div.find_all('a'):
        for sib in i.next_siblings:
            placename = i.contents[0].encode('latin1').decode('utf-8')
            if sib.name == 'span':
                temp = sib.text.encode('latin1').decode('utf-8')
                fields = temp.split('|')
                chile_csv.writerow([ftfy.fix_text(placename), ftfy.fix_text(fields[0]), ftfy.fix_text(fields[1]), ftfy.fix_text(fields[2]), ftfy.fix_text(fields[3]), "Orography"])
            elif sib.name == 'ul':
                break

    if b == 50 or b == 100 or b == 150:
        sleep(10)