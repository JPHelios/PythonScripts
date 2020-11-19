import requests
from bs4 import BeautifulSoup

array_URL = "https://www.amazon.de/ALED-LIGHT-Wasserdichtes-Kontrolliertes-Lichtschl%C3%A4uche/dp/B0781MCM5Z/ref=sr_1_5?__mk_de_DE=%C3%85M%C3%85%C5%BD%C3%95%C3%91&dchild=1&keywords=bluetooth+led+streifen&qid=1605775693&sr=8-5"
headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36 Edg/86.0.622.63'}

page = requests.get(array_URL, headers=headers)
soup = BeautifulSoup(page.content, "lxml")

price = soup.find(id="priceblock_ourprice").get_text().strip()
print(f"This is the price with id: {price}")

class_price = soup.find('span', {'class': 'a-size-medium a-color-price priceBlockBuyingPriceString'}).get_text()
print(f"This is the price with span: {class_price}")

sparpreis = soup.find('span', {'class': 'a-span12 a-color-price a-size-base priceBlockSavingsString'})
print(f"Das ist ein weiterer Versuch für den Sparpreis: {sparpreis}:")

gesamt = soup.find(id="regularprice_savings").get_text().strip()

gesamt = gesamt.replace('Sie sparen:', '').strip()
print(gesamt)

test = gesamt[-4: -2]
print(test)

test =int(test)
print(test)