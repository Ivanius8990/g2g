from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import sqlite3




conn2 = sqlite3.connect('prices.db', check_same_thread=False)
cur2 = conn2.cursor()
cur2.execute("""CREATE TABLE IF NOT EXISTS prices_WOW(
   serv_id INT PRIMARY KEY,
   serv_name TEXT,
   min_prise TEXT,
   midl_prise TEXT,
   midl_stock TEXT,
   sellers_amaunt TEXT);
""")
conn2.commit()


s=Service('C:\webdriver\chromedriver.exe')
driver = webdriver.Chrome(service=s)
url='https://funpay.com/chips/2/'
driver.get(url)
wait = WebDriverWait(driver, 10) ###все wait ждут пока загрузится элемент


n=5###количество продавцов
prices=[]
wait.until(EC.presence_of_element_located((By.TAG_NAME, 'option')))
serv_name = driver.find_elements(By.TAG_NAME, 'option')
for i in range(1):
    serv_name[i+1].click()
    body=driver.find_element(By.TAG_NAME, 'body')
    data=body.text[(body.text.find('\n'+serv_name[i+1].text)):(body.text.rfind('₽'))]
    data_list=data.split('₽')
    midl_prise = 0
    midl_stock = 0
    min_price=0
    price_list=[]
    min_price=[]
    for j in range(n):
        dat=data_list[j].split('\n')
        midl_prise=midl_prise+float(dat[6])*float(dat[5].replace(' ', ''))
        midl_stock=midl_stock+float(dat[5].replace(' ', ''))
        min_price.append(dat[6])
    midl_prise=round(midl_prise/midl_stock,6)
    midl_stock=midl_stock/n/1000
    min_price=min(min_price)
    price_list.append(serv_name[i+1].text)
    price_list.append(min_price)
    price_list.append(midl_prise)
    price_list.append(midl_stock)

    print(price_list)





driver.close()
driver.quit()