from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import sqlite3


s=Service('C:\webdriver\chromedriver.exe')
driver = webdriver.Chrome(service=s)
url='https://funpay.com/chips/2/'
driver.get(url)
wait = WebDriverWait(driver, 10) ###все wait ждут пока загрузится элемент

##поиск регионов
servers=[]
wait.until(EC.presence_of_element_located((By.TAG_NAME, 'option')))
serv_name = driver.find_elements(By.TAG_NAME, 'option')
for i in range(1):
    serv_name[i+1].click()
    print(serv_name[i+1].text)
    gg=driver.find_element(By.TAG_NAME, 'body')
    ff=gg.text[(gg.text.find('Сервер Сторона Продавец Наличие Цена')):(gg.text.rfind('₽')+1)]
    yy=ff.split('₽')

    print(yy)




driver.close()
driver.quit()