# Imports
import requests
from bs4 import BeautifulSoup
import re

# Define the FISH Day Shift PTO calander
URL = "https://calendar.google.com/calendar/u/0/htmlembed?src=cytogenfishmgmt@gmail.com&amp;ctz=America/Chicago"

# Define the request for the URL page info, parse it using html5lib, and print it to the terminal
r = requests.get(URL)
soup = BeautifulSoup(r.content, 'html5lib')
#print(soup.prettify())

# works to give title of page (1 FISH Days)
title = soup.find('title')
print(title.string)

list = []

# Get FLEX and PTO spots on calander
list.append(soup.find('span', class_='event-summary').string)
 



#name = soup.find('span', class_='event-summary')
#print(name.string)