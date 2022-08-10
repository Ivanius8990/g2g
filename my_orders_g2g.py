import time

import webdriver-manager
import pickle
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
chrome_options = Options()
'''chrome_options.add_argument("--disable-extensions")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--headless")'''
s = Service('C:\webdriver\chromedriver.exe')




import json

def save_cookie(driver, path):
    with open(path, 'w') as filehandler:
        json.dump(driver.get_cookies(), filehandler)



url = 'https://vk.com'
driver = webdriver.Chrome(options=chrome_options, service=s)
driver.get(url)
driver.delete_all_cookies()


def load_cookie(driver):
    with open("cookie", 'rb') as cookiesfile:
        cookies = pickle.load(cookiesfile)
        for cookie in cookies:
            print(cookie)
            driver.add_cookie(cookie)


driver = webdriver.Chrome(ChromeDriverManager().install())
url = 'https://www.Youtube.com'
driver.get(url)
# first try to login and generate cookies after that you can use cookies to login eveytime
load_cookie(driver)
# Do you task here
save_cookie(driver)
driver.quit()