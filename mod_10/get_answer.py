import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeOutException

from bs4 import Beautiful Soup
from urllib.parse import urlparse
import sys

class Fetcher:
    """docstring for Fetcher"""
    def __init__(self, url):
        self.driver = webdriver.PhantomJS()
        self.driver.wait = WebDriverWait(self.driver, 5)
        self.url = url

    def lookup(self):
        self.driver.get(self.url)
        try:
            ip = self.driver.wait.until(EC.presence_of_element_located(
                By.CLASS_NAME, 'gsfi'))
        except:
            print('Failed')

        soup = BeautifulSoup(self.driver.page_source, 'html.parser')
        answer = soup.find_all(class_='_sPg')

        if not answer:
            answer = soup.find_all(class_='_m3b')

        if not answer:
            answer = 'I dont know'

        self.driver.quit()
        return answer[0].get_text()

