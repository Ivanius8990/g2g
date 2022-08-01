from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
import time

s=Service('C:\webdriver\chromedriver.exe')
driver = webdriver.Chrome(service=s)
url='https://www.g2g.com/categories/wow-gold'
driver.get(url)
html = driver.page_source

button = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div[1]/div[5]/div[1]/div/div/div/div[1]/div[3]/div[1]/div/div[3]/div[1]/div/div/button').click()
time.sleep(10)
cl_button = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div[1]/div[5]/div[1]/div/div/div/div[3]/aside/div[1]/div/div[2]/div')
elems = cl_button.find_elements(By.TAG_NAME,"a")
for elem in elems:
    print(elem.get_attribute("href"))


driver.close()
driver.quit()