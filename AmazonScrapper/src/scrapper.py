import requests
import array
import sys
import smtplib
import email
import re
import pickle

from bs4 import BeautifulSoup
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

array_URL = pickle.load(open("data.txt", "rb"))
headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36 Edg/86.0.622.63'}


def check_price(URL):
    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, "lxml")

    title = soup.find(id="productTitle").get_text().strip()
    price = soup.find(id="priceblock_ourprice").get_text().strip()
    saving = soup.find(id="regularprice_savings").get_text().strip()

    saving = saving.replace('Sie sparen:', '').strip()
    saving = int(saving[-4:-2])
    
    print(f"Sie sparen so viel %: {saving}")

    price = price.replace('\xa0€', '')
    price = price.replace(',', ".")
    converted_price = float(price)

    if(converted_price < 100):
        send_mail(title, price, URL)

def send_mail(title, price, URL):

    msg = MIMEText("Das Produkt auf deiner Liste ist im Angebot: \n\n" + title + "\n\nPreis: " + price +"€"+ "\n\n Prüfe auf Amazon nach, indem du diesem Link folgst: \n" + URL)

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