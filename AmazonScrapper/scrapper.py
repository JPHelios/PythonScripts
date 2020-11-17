import requests
from bs4 import BeautifulSoup

import array

import sys
import smtplib
import email
import re
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

array_URL = [
    "https://www.amazon.de/Kingston-HyperX-Cloud-Gaming-Kopfh%C3%B6rer/dp/B00SAYCXWG/ref=sr_1_1?__mk_de_DE=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=E6E7D45G1DUV&dchild=1&keywords=hyper+cloud+x+ii&qid=1605177249&sprefix=hyper+cloud%2Caps%2C380&sr=8-1",
    "https://www.amazon.de/ALED-LIGHT-Wasserdichtes-Kontrolliertes-Lichtschl%C3%A4uche/dp/B0781MCM5Z/ref=sr_1_6?__mk_de_DE=%C3%85M%C3%85%C5%BD%C3%95%C3%91&dchild=1&keywords=Bluetooth+LED+Streifen&qid=1605254811&sr=8-6"
]

#URL = 'https://www.amazon.de/Kingston-HyperX-Cloud-Gaming-Kopfh%C3%B6rer/dp/B00SAYCXWG/ref=sr_1_1?__mk_de_DE=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=E6E7D45G1DUV&dchild=1&keywords=hyper+cloud+x+ii&qid=1605177249&sprefix=hyper+cloud%2Caps%2C380&sr=8-1'

headers = {
    "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36 Edg/86.0.622.63'}


def check_price(URL):
    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, "lxml")

    title = soup.find(id="productTitle").get_text().strip()
    price = soup.find(id="priceblock_ourprice").get_text().strip()

    converted_price = float(price[0:2])

    print(title)
    print(converted_price)

    if(converted_price < 100):
        send_mail(title, price, URL)

def send_mail(title, price, URL):

    print('Die Daten sind angekommen für: ' + title)
    print(price)
    print(URL)

    msg = MIMEText("Das Produkt auf deiner Liste ist im Angebot: \n\n" + title + "\n\n Prüfe auf Amazon nach, indem du diesem Link folgst: \n" + URL)

    msg['Subject'] = 'Ein Produkt ist im Angebot!'
    msg['From'] = 'jojo.peters01@googlemail.com'
    msg['To'] = 'johannes.f.peters@gmx.de'

    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.login('jojo.peters01@googlemail.com', 'xmzqvjpmrhgbwrfy')

    server.send_message(msg)
    server.quit()


for i in range(0, len(array_URL)):
    URL = array_URL[i]
    check_price(URL)