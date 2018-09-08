import subprocess
import os
import requests
from bs4 import BeautifulSoup
from get_answer import Fetcher

class Commander:
    """docstring for Commander"""
    def __init__(self):
        self.confirm = ['yes','affirmative','si','sure',
                        'do it','yeah','confirm']
        self.cancel = ['no','negative','negative soldier','do not'
                        ,'wait','cancel']


    def discover(self, text):
        if 'what' in text and 'name' in text:
            if 'my' in text:
                self.respond('You have not told me your name yet')
            else:
                self.respond('My name is python commander. How are you?')

        if 'launch' or 'open' in text:
            app = text.split(' ', 1)[-1]
            self.respond('Opening '+app)
            os.system('open -a' + app + '.app')

        else:
            f = Fetcher('https://www.google.com/search?safe=active&source=hp&ei=ccCTW-SCNoLjsAfo_IrQBQ&q=' + text.replace(" ", "+"))
            ans = f.lookup()
            self.respond(ans)

    def respond(self, respond):
        print(respond)
        subprocess.call('say'+respond, shell=True)
