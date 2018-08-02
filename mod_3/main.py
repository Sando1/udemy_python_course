"""practice code for learning Beautiful Soup"""

from bs4 import BeautifulSoup
import requests

#first target
search = input('Enter search')
param = {'q': search}
r = requests.get('http://www.bing.com/search', params=param)
soup= BeautifulSoup(r.text, 'html.parser')

results = soup.find('ol', {'id':'b_results'})

links = results.findAll('li', {'class':'b_algo'})

for item in links:
    item_text = item.find('a').text
    item_href = item.find('a').attrs['href']

    if item_text and item_href:
        print(item_text+'  '+item_href)
        #parent parsing
        #print('Parent : {}'.format(item.find('a').parent))
        #print('Parent : {}'.format(item.find('a').parent.parent.find('p').text))

        #children parsin
        #children = item.children
        #for child in children:
        #    print('Children : {}'.format(child))

        #parsing siblings
        #print('Sibling : {}'.format(item.next_sibling))
