import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
from selenium import webdriver


url = 'https://www.g2g.com/categories/wow-gold?region_id=dfced32f-2f0a-4df5-a218-1e068cfadffa'
options = webdriver.FirefoxOptions()
options.add_argument('--headless')
options.binary_location = r"C:\Program Files\Mozilla Firefox\firefox.exe"
driver = webdriver.Firefox(executable_path=r'C:\webdriver\geckodriver.exe',options=options)
driver.get(url)
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
reg=soup.find('body', class_='desktop no-touch body--light q-body--dialog q-body--prevent-scroll')
print(soup)


