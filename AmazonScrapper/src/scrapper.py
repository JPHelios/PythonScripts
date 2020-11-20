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


####################################################################################################

def send_mail(title, price, URL, saving_price, original_price):

    msg = MIMEText(f"""
        Dieses Produkt aus deiner Liste ist im Angebot: 
        \n\n{title} 
        \n\nPreis: {price}€
        \nOriginalpreis: {original_price}€
        \nSie sparen dabei: {saving_price}€
        \n\n Prüfe auf Amazon nach, indem du diesem Link folgst: 
        \n\n{URL}""")

    msg['Subject'] = 'Ein Produkt ist im Angebot!'
    msg['From'] = 'jojo.peters01@googlemail.com'
    msg['To'] = 'johannes.f.peters@gmx.de'

    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.login('jojo.peters01@googlemail.com', 'xmzqvjpmrhgbwrfy')

    server.send_message(msg)
    server.quit()

######################################################################################



array_URL = pickle.load(open("data.txt", "rb"))
headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36 Edg/86.0.622.63'}

for i in range(0, len(array_URL)):
    URL = array_URL[i]
    #check_price(URL)

    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, "lxml")

    title = soup.find(id="productTitle").get_text().strip()
    price = soup.find(id="priceblock_ourprice").get_text().strip()
    saving_text = soup.find(id="regularprice_savings")
    
    if saving_text is None: continue

    saving_text = saving_text.get_text().strip()
    saving_text = saving_text.replace('Sie sparen:', '').strip()
    saving_text = saving_text.replace(',', '.')

    saving_percentage = int(saving_text[-4:-2])
    saving_price = saving_text[:-7:].strip()
    
    price = price.replace('\xa0€', '')
    price = price.replace(',', ".")
    price = price

    original_price = float(saving_price) + float(price)

    if(saving_percentage > 5):
        send_mail(title, price, URL, saving_price, original_price)