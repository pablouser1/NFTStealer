import json
from os import getenv
from random import randint
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

from nftstealer.models import Nft

TIMEOUT = 5

class Stealer:
    driver: webdriver.Firefox

    def __init__(self):
        options = Options()
        options.headless = True
        self.driver = webdriver.Firefox(firefox_binary=getenv('FIREFOX_BIN', '/usr/bin/firefox'), options=options)
    
    def randomLink(self)-> str:
        print("Loading assets...")
        link = ""
        self.driver.get("https://opensea.io/assets")
        try:
            WebDriverWait(self.driver, TIMEOUT).until(EC.presence_of_element_located((By.ID, 'main')))
            nfts = self.driver.find_elements(By.CSS_SELECTOR, 'a.styles__StyledLink-sc-l6elh8-0.ekTmzq.Asset--anchor')
            if len(nfts) > 0:
                rand = randint(0, len(nfts) - 1)
                nft = nfts[rand]
                link = nft.get_attribute('href')
            else:
                print("Couldn't find any nfts")
        except TimeoutException:
            print("Couldn't load page")
        finally:
            return link

    def getNft(self, link: str)-> Nft:
        nft = Nft()
        print("Screenshooting...")
        self.driver.get(link)
        try:
            WebDriverWait(self.driver, TIMEOUT).until(EC.presence_of_element_located((By.ID, 'main')))
            # Get NFT Id
            next_script = self.driver.find_element(By.ID, '__NEXT_DATA__')
            next_string = next_script.get_attribute('innerText')
            data = json.loads(next_string)
            png = self.driver.get_screenshot_as_png()
            nft.id = data["query"]["tokenId"]
            nft.data = png
        except TimeoutException:
            print("Couldn't load page")
        finally:
            return nft
    
    def cleanup(self):
        self.driver.close()
