import requests
from bs4 import BeautifulSoup as bs

# Load webpage content
re = requests.get(
    'https://keithgalli.github.io/web-scraping/example.html')
soup = bs(re.content, 'html.parser')
# print(soup.prettify())

first_header = soup.find("h2")
print(first_header)

# headers = soup.find_all("h2")
# print(headers)
