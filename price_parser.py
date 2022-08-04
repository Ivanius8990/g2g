from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import sqlite3


'''conn = sqlite3.connect('urls.db')
cur = conn.cursor()
cur.execute("""SELECT * from urls_WOW""")
records = cur.fetchall()

print(records)'''



###url и сколько брать продавцов
def prise_parsing(url,n):
    s=Service('C:\webdriver\chromedriver.exe')
    driver = webdriver.Chrome(service=s)
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
    for i in range(1,n+1):
        price_list.append(prices[i].text)
    #print(price_list)

    stock_list=[]
    min_purch_list=[]
    wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'offers-bottom-attributes')))
    stock=driver.find_elements(By.CLASS_NAME, 'offers-bottom-attributes')
    for i in range(2,n*4+2,4):
        stock_list.append(stock[i].text)
    #print(stock_list)

    for i in range(4,n*4+4,4):
        min_purch_list.append(stock[i].text)
    #print(min_purch_list)

    for j in range(n):
        main_list.append((server_name,price_list[j],stock_list[j],min_purch_list[j]))
    driver.close()
    driver.quit()
    return main_list

url='https://www.g2g.com/offer/ZuluhedDEHorde?service_id=lgc_service_1&brand_id=lgc_game_2299&region_id=ac3f85c1-7562-437e-b125-e89576b9a38e&fa=lgc_2299_dropdown_17%3Algc_2299_dropdown_17_42205&sort=lowest_price&include_offline=1'
n = 5
gg=prise_parsing(url,5)
print(gg)