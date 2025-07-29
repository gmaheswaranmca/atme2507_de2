import requests 
from bs4 import BeautifulSoup 
url = 'https://quotes.toscrape.com/'

response=requests.get(url)
html = response.text
#print(html)

soup = BeautifulSoup(html, 'html.parser')
quotes_div = soup.find_all('div', class_='quote')
for div in quotes_div:
    quote_text = div.find('span', class_='text').text
    author_name = div.find('small', class_='author').text
    print(quote_text)
    print('---By ', author_name)
    print()
