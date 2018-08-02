from bs4 import BeautifulSoup
import requests
from PIL import Image
from io import BytesIO
import os


while True:
    search = input('Enter search: ')

    if search == 'quit':
        break

    param = {'q': search}
    dir_name = search.replace(" ","_").lower()
    r = requests.get('http://www.bing.com/images/search', params=param)
    soup= BeautifulSoup(r.text, 'html.parser')

    if not os.path.isdir(dir_name):
        os.makedirs(dir_name)

    links = soup.findAll('a', {'class':'thumb'})
    for link in links:
        try:
            img_obj = requests.get(link.attrs['href'])
            print('Getting'+link.attrs['href'])
            title = link.attrs['href'].split('/')[-1]
            img = Image.open(BytesIO(img_obj.content))
            img.save('./'+dir_name+'/'+title,img.format)
        except:
            print('Could Not Save Image')
