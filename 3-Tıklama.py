

from selenium import webdriver
from selenium.webdriver.edge.service import Service

# servis bağlantısını edge olarak driver dosyasıyla bağlıyoruz.
servic=Service(".\\msedgedriver.exe")
# kullanacağımız tarayıcıyı webdriver class bağlıyarak servis olarak
# atadığımız değişkeni webdriver servisi olarak tanımladık.
driver=webdriver.Edge(service=servic)
#driver.get("http://duckduckgo.com")

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
import time

# wait=WebDriverWait(driver,15)
# try:
    
    
#     # driver.maximize_window()
#     # search_box=driver.find_element(By.ID,"searchbox_homepage")
#     search_box=wait.until(expected_conditions.element_to_be_clickable((By.ID,"searchbox_input")))
#     #search_box=driver.find_element((By.XPATH,"//*[@id="searchbox_homepage"]/div/div"))
#     search_box.send_keys("selenium")
    
#     search_button=wait.until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, "[aria-label='Search']")))
#     #search_button=wait.until(expected_conditions.element_to_be_clickable((By.CLASS_NAME,"searchbox_iconWrapper__suWUe")))
#     search_button.click()
    
#     select_search=wait.until(expected_conditions.element_to_be_clickable((By.ID,"r1-3")))
#     select_search.click()
    
#     # print("Elemente başarıyla tıklandı!")
#     time.sleep(20)
    
# except Exception as ex:
#     print("elemente tıklanamadı.",str(ex))


driver.get("http://google.com")
try:
    # search_box=driver.find_element((By.ID,"APjFqb"))
    # search_box=driver.find_element((By.CLASS_NAME,"a4bIc"))
    # search_box=driver.find_element((By.CLASS_NAME,"gLFyf"))
    # search_box=driver.find_element(By.XPATH,"//*[@id='APjFqb']")
    search_box=driver.find_element(By.NAME,"q")
    search_box.send_keys("selenium")
    # search_box.send_keys(Keys.ENTER)
    search_button=driver.find_element(By.CLASS_NAME,"iblpc")
    search_button.click()
    
    print("başarılı")
    time.sleep(100)
    
except Exception as ex:
    print("elemente tıklanamadı.",str(ex))






