from bs4 import BeautifulSoup
import requests

response = requests.get('https://www.zillow.com/homedetails/2515-Lourdes-Dr-W-Jacksonville-FL-32210/44414305_zpid/')
yc_webpage = response.text
soup =BeautifulSoup(yc_webpage, 'html.parser')
print(soup)

