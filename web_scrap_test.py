import requests
import re
from bs4 import BeautifulSoup

# First method of scrapig, simple and dirty (with requests and regex)
# # get the data
# data = requests.get('xxxxx')
#
# #extract the phone numbers, emails and so on
#
# phones = re.findall(r'(\(?[0-9]{3}\)?(?:\-|\s|\.)?[0-9]{3}(?:\-|\.)[0-9]{4})', data.text)
# emails = re.findall(r'([\d\w\.]+@[\d\w\.\-]+\.\w+)', data.text)
#
# print(phones, emails)

# Scraping with beautiful soup

data = requests.get('https://raw.githubusercontent.com/engineer-man/youtube/master/042/scrape.html')

# load data into bs4
soup = BeautifulSoup(data.text, 'html.parser')

# get data simply by looking for each tr
scrapped_data = []
for tr in soup.find_all('tr'):
    values = [td.text for td in tr.find_all('td')]
    scrapped_data.append(values)

print(scrapped_data)

# get data simply by looking for each tr
scrapped_data_special = []
for tr in soup.find_all('tr', {'class': 'special'}):
    values_special = [td.text for td in tr.find_all('td')]
    scrapped_data_special.append(values_special)
print(scrapped_data_special)

# get data within specific element
specific_element = []
div = soup.find('div', {'class': 'special_table'})
for tr in div.find_all('tr'):
    values_special_class = [td.text for td in tr.find_all('td')]
    specific_element.append(values_special_class)
print(specific_element)

