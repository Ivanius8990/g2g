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
import concurrent.futures




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

###url,сколько брать продавцов и id сервера. Функция добавляет данные в БД
def prise_parsing(url,n,serv_id):
    s=Service('C:\webdriver\chromedriver.exe')
    driver = webdriver.Chrome(options=chrome_options,service=s)
    driver.get(url)
    wait = WebDriverWait(driver, 10) ###все wait ждут пока загрузится элемент

    main_list=[]
    wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'main__title-skin')))
    server_name = driver.find_element(By.CLASS_NAME, 'main__title-skin').text
    #print(server_name)

    ###метод доставки
    '''wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'icon-devliry-details')))
    delivery = driver.find_elements(By.CLASS_NAME, 'icon-devliry-details')
    for i in delivery:
        print(i.text)'''

    price_list=[]
    wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'offer-price-amount')))
    prices=driver.find_elements(By.CLASS_NAME, 'offer-price-amount')
    if len(prices)<n+1:
        n=len(prices)-1
    for i in range(1,n+1):
        price_list.append(prices[i].text)
    #print(price_list)

    stock_list=[]
    wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'offers-bottom-attributes')))
    stock=driver.find_elements(By.CLASS_NAME, 'offers-bottom-attributes')
    for i in range(2,n*4+2,4):
        stock_list.append(stock[i].text)
    #print(stock_list)

    ###минимальная сумма заказа
    '''min_purch_list=[]
    for i in range(4,n*4+4,4):
        min_purch_list.append(stock[i].text)
    #print(min_purch_list)'''

    mid_price=0
    mid_stock=0
    for i in range(n):
        stock_list[i]=(stock_list[i][:stock_list[i].find('K')]).replace(',','')
        mid_price=mid_price+(float(price_list[i])*float(stock_list[i]))
        mid_stock=mid_stock+float(stock_list[i])
    serv_id=main_list.append(serv_id)
    main_list.append(server_name)
    min_price = main_list.append(min(price_list))
    midl_price = main_list.append(round(mid_price / mid_stock, 6))
    midl_stock = main_list.append(int(mid_stock / n))
    sellers_amaun = main_list.append(len(prices) - 1)
    print(main_list)
    cur2 = conn2.cursor()
    cur2.execute("REPLACE INTO prices_WOW VALUES(?, ?, ?, ?, ?, ?);", main_list)
    conn2.commit()
    cur2.close()
    driver.close()
    driver.quit()
    return main_list

with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
    futures = []
    conn = sqlite3.connect('urls.db')
    cur = conn.cursor()
    cur.execute("""SELECT * from urls_WOW WHERE serv_id LIKE 'RU%'""")
    records = cur.fetchall()
    for row in records:
        serv_id=row[0]
        url=row[1]
        futures.append(executor.submit(prise_parsing, url, 5, serv_id))
    for future in concurrent.futures.as_completed(futures):
        print(future.result())
    conn.commit()
cur.close()




