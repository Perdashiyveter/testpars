from bs4 import BeautifulSoup
import requests

url = 'https://yandex.ru/pogoda/saratov?lat=51.533561&lon=46.034265'
response = requests.get(url)
print(response)
bs = BeautifulSoup(response.text,"lxml")
print(bs)
temp = bs.find('span','temp__value temp__value_with-unit')
print(temp.text)