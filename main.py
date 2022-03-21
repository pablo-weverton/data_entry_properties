from bs4 import BeautifulSoup
import requests
from fill_data import Fill

headers = {
    'Accept-Language': SEU ACCEPT LANGUAGE,
    'User-Agent': SEU USER AGENT
}

index = requests.get('https://www.zillow.com/homes/?searchQueryState=%7B"pagination"%3A%7B%7D%2C"mapBounds"%3A%7B"west"'
                     '%3A-122.51721382141113%2C"east"%3A-122.31945991516113%2C"south"%3A37.705757205454226%2C"north"%'
                     '3A37.847680327769055%7D%2C"isMapVisible"%3Atrue%2C"filterState"%3A%7B"price"%3A%7B"min"%3A0%2C"max'
                     '"%3A872627%7D%2C"mp"%3A%7B"min"%3A0%2C"max"%3A3000%7D%2C"beds"%3A%7B"min"%3A1%7D%2C"fsba"%3A%7B"'
                     'value"%3Afalse%7D%2C"nc"%3A%7B"value"%3Afalse%7D%2C"fore"%3A%7B"value"%3Afalse%7D%2C"cmsn"%3A%7B"'
                     'value"%3Afalse%7D%2C"fr"%3A%7B"value"%3Atrue%7D%2C"ah"%3A%7B"value"%3Atrue%7D%7D%2C"isListVisible"'
                     '%3Atrue%2C"mapZoom"%3A12%7D',
                     headers=headers)

soup = BeautifulSoup(index.text, 'html.parser')

# Get Links of the Properties

all_links = soup.select('.list-card-info a')
links_formatted = [link.get('href') for link in all_links]

# Get Address of the Properties

all_address = soup.select('.list-card-info address')
address_formatted = [address.text for address in all_address]

# Get Prices of the Properties

all_prices = soup.select('.list-card-price')
prices_formatted = [price.text for price in all_prices]

# Create the object Pull_data passing the link, address and price per month

for i in range(len(address_formatted)):
    if '/mo' not in prices_formatted[i]:
        prices_formatted[i] = prices_formatted[i] + '/mo'
        if 'bd' in prices_formatted[i]:
            prices_formatted[i] = prices_formatted[i].split('+')[0] + '/mo'
    if 'https' not in links_formatted[i]:
        links_formatted[i] = 'https://www.zillow.com' + links_formatted[i]
    if prices_formatted[i] == 0:
        continue
    pull_data = Fill(address_formatted[i], prices_formatted[i], links_formatted[i])








