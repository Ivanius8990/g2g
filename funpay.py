from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
chrome_options = Options()
chrome_options.add_argument("--disable-extensions")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--headless")
import sqlite3


def name_replace(name):
    encode_name = name
    simb = '[] ()-'  ###символы которые надо удалить
    for char in simb:
        encode_name = encode_name.replace(char, '')
    return encode_name

conn = sqlite3.connect('prices_funpay.db', check_same_thread=False)
cur = conn.cursor()
cur.execute("""CREATE TABLE IF NOT EXISTS prices_WOW_funpay(
   serv_name TEXT PRIMARY KEY,
   min_prise TEXT,
   midl_prise TEXT,
   midl_stock TEXT);
""")
conn.commit()


n=5
url = 'https://funpay.com/chips/2/'


s = Service('C:\webdriver\chromedriver.exe')
driver = webdriver.Chrome(options=chrome_options,service=s)
driver.get(url)
wait = WebDriverWait(driver, 10)  ###все wait ждут пока загрузится элемент

wait.until(EC.presence_of_element_located((By.TAG_NAME, 'option')))
serv_name = driver.find_elements(By.TAG_NAME, 'option')
for i in range(len(serv_name)-3):
    serv_name[i + 1].click()
    body = driver.find_element(By.TAG_NAME, 'body')
    data = body.text[(body.text.find("Цена/1000")):(body.text.rfind('₽'))]
    data_list = data.split('₽')
    midl_prise = 0
    midl_stock = 0
    min_price = 0
    price_list = []
    min_price = []
    for j in range(n):
        dat = data_list[j].split('\n')
        midl_prise = midl_prise + float(name_replace(dat[6])) * float(name_replace(dat[5]))
        midl_stock = midl_stock + float(dat[5].replace(' ', ''))
        min_price.append(dat[6])
    midl_prise = round(midl_prise / midl_stock, 6)
    midl_stock = int(midl_stock / n / 1000)
    min_price = min(min_price)
    price_list.append(serv_name[i + 1].text)
    price_list.append(min_price)
    price_list.append(midl_prise)
    price_list.append(midl_stock)
    cur = conn.cursor()
    cur.execute("REPLACE INTO prices_WOW_funpay VALUES(?, ?, ?, ?);", price_list)
    conn.commit()
    cur.close()
    print(price_list)

driver.close()
driver.quit()