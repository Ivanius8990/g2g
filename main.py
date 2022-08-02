from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains



s=Service('C:\webdriver\chromedriver.exe')
driver = webdriver.Chrome(service=s)
url='https://www.g2g.com/categories/wow-gold'
driver.get(url)
wait = WebDriverWait(driver, 10) ###все wait ждут пока загрузится элемент

##поиск регионов
region=[]
servers=[]
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
    button2 = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div[1]/div[5]/div[1]/div/div/div/div[1]/div[3]/div[1]/div/div[3]/div[1]/div/div/div/div/button').click()
    wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/div/div[1]/div[1]/div[5]/div[1]/div/div/div/div[1]/div[3]/div[1]/div/div[3]/div[1]/div/div/div/div/div/aside/div[1]/div/div[2]/div/div[2]/div[13]/span')))
    button3 = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div[1]/div[5]/div[1]/div/div/div/div[1]/div[3]/div[1]/div/div[3]/div[1]/div/div/div/div/div/aside/div[1]/div/div[2]/div/div[2]/div[13]/span').click()
    wait.until(EC.visibility_of_element_located((By.XPATH,'/html/body/div[1]/div/div[1]/div[1]/div[5]/div[1]/div/div/div/div[1]/div[3]/div[1]/div/div[3]/div[1]/div/div/div/div/div/aside/div[1]/div/div[2]/div/div[2]')))
    cl_button2 = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div[1]/div[5]/div[1]/div/div/div/div[1]/div[3]/div[1]/div/div[3]/div[1]/div/div/div/div/div/aside/div[1]/div/div[2]/div/div[2]')


### находим все чекбоксы, прокручиваем и щелкаем по ним
    elems2 = cl_button2.find_elements(By.CLASS_NAME,"text-body2")
    for i,elem in enumerate(elems2):
        driver.execute_script("arguments[0].scrollIntoView();", elem)
        elem.click()
        servers.append(elem.text)


        print(elem.text)
    print(i+1)




driver.close()
driver.quit()