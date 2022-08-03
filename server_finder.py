from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import sqlite3


conn = sqlite3.connect('servers.db')
cur = conn.cursor()
cur.execute("""CREATE TABLE IF NOT EXISTS servers_WOW(
   serv_id INT PRIMARY KEY,
   serv_name TEXT,
   reg TEXT,
   serv_index TEXT);
""")
conn.commit()

s=Service('C:\webdriver\chromedriver.exe')
driver = webdriver.Chrome(service=s)
url='https://www.g2g.com/categories/wow-gold'
driver.get(url)
wait = WebDriverWait(driver, 10) ###все wait ждут пока загрузится элемент

##поиск регионов
region=[]
wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div[1]/div[1]/div[5]/div[1]/div/div/div/div[1]/div[3]/div[1]/div/div[3]/div[1]/div/div/button')))
button = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div[1]/div[5]/div[1]/div/div/div/div[1]/div[3]/div[1]/div/div[3]/div[1]/div/div/button').click()
wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div[1]/div[1]/div[5]/div[1]/div/div/div/div[3]/aside/div[1]/div/div[2]/div')))
cl_button = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div[1]/div[5]/div[1]/div/div/div/div[3]/aside/div[1]/div/div[2]/div')
elems = cl_button.find_elements(By.TAG_NAME,"a")
for elem in elems:
    region.append(elem.get_attribute("href"))
print(region)

###поиск серверов в регионах
for i in region:
    driver.get(i)
    wait.until(EC.visibility_of_element_located((By.XPATH,'/html/body/div[1]/div/div[1]/div[1]/div[5]/div[1]/div/div/div/div[1]/div[3]/div[1]/div/div[3]/div[1]/div/div/div/div/button')))
    reg=driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div[1]/div[5]/div[1]/div/div/div/div[2]/div/div/div').text###ищет имя региона
    reg=(reg[reg.find(": ") + 2:])###сокращает имя региона
    button2 = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div[1]/div[5]/div[1]/div/div/div/div[1]/div[3]/div[1]/div/div[3]/div[1]/div/div/div/div/button').click()
    wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/div/div[1]/div[1]/div[5]/div[1]/div/div/div/div[1]/div[3]/div[1]/div/div[3]/div[1]/div/div/div/div/div/aside/div[1]/div/div[2]/div/div[2]/div[13]/span')))
    button3 = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div[1]/div[5]/div[1]/div/div/div/div[1]/div[3]/div[1]/div/div[3]/div[1]/div/div/div/div/div/aside/div[1]/div/div[2]/div/div[2]/div[13]/span').click()
    wait.until(EC.visibility_of_element_located((By.XPATH,'/html/body/div[1]/div/div[1]/div[1]/div[5]/div[1]/div/div/div/div[1]/div[3]/div[1]/div/div[3]/div[1]/div/div/div/div/div/aside/div[1]/div/div[2]/div/div[2]')))
    cl_button2 = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div[1]/div[5]/div[1]/div/div/div/div[1]/div[3]/div[1]/div/div[3]/div[1]/div/div/div/div/div/aside/div[1]/div/div[2]/div/div[2]')

    ### находим все чекбоксы, прокручиваем и щелкаем по ним. Сохраняет имена серверов
    server_name = []
    elems2 = cl_button2.find_elements(By.CLASS_NAME,"text-body2")
    for elem in elems2:
        driver.execute_script("arguments[0].scrollIntoView();", elem)
        elem.click()
        server_name.append(elem.text)
    driver.find_element(By.XPATH,'/html/body/div[1]/div/div[1]/div[1]/div[5]/div[1]/div/div/div/div[1]/div[3]/div[1]/div/div[3]/div[1]/div/div/div/div/div/aside/div[1]/div/div[3]/div/div[2]/button').click()
    cur_url=str(driver.current_url)###получает url адрес в браузере
    print(cur_url)
    cut_url_first = cur_url[:(cur_url.find("%3A") + 3)]
    cut_url_first = cut_url_first[(cut_url_first.find("&fa")+1):]### первая часть в адрес которая повторяется во всех серверах региона

    servers = []
    cut_url = cur_url[cur_url.find("%3A") + 3:]
    servers = cut_url.split(",")
    servers=[f'{cut_url_first}{j}' for j in servers]###склеивает первую часть адреса с остальной

    i = i[i.find("region_id"):]###преобразовывает url в индекс региона

    print(servers)
    lst=[]###делает кортеж списков для БД
    for j,serv in enumerate(servers):
        lst.append((reg+str(j+1),server_name[j],i,servers[j]))
    cur.executemany("REPLACE INTO servers_WOW VALUES(?, ?, ?, ?);", lst)
conn.commit()
cur.close()

driver.close()
driver.quit()