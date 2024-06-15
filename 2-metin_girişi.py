
from selenium import webdriver

# from selenium.webdriver.chrome.service import Service
from selenium.webdriver.edge.service import Service
#from selenium.webdriver.firefox.service import Service


#servic=Service(".\\selenium\\chromedriver.exe")
servic=Service(".\\selenium\\msedgedriver.exe")
#servic=Service(".\\selenium\\geckodriver.exe")



#driver=webdriver.Chrome(service=servic)
driver=webdriver.Edge(service=servic)
#driver=webdriver.Firefox(service=servic)


driver.get("http://www.duckduckgo.com")
#driver.get("http://www.google.com/maps")

import time

# BUNDAN SONRA WEB ELEMENTİN FOKSİYONLARIYLA ÇALIŞICAZ. 

from selenium.webdriver.common.by import By
# burada sayfadaki bazı nesne bölümlerine seçerek tıklama işlemlerini yapıcaz.
# öncelik "id" veriyorduk.
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys

# driver.back()

# Arama kutusunun görünür olmasını bekleyin
waits = WebDriverWait(driver,60)
try:
    search_box = waits.until(EC.visibility_of_element_located((By.ID, "searchbox_input")))
    search_box.click()
    search_box.send_keys("python")
    print("Elemente başarıyla tıklandı!")
    # enter tuşuna basar
    search_box.send_keys(Keys.ENTER)
    time.sleep(120)
except Exception as ex:
    print("elemente tıklanamadı.",str(ex))
    
    


    
    
    

# box=driver.find_element(By.ID,"searchbox_homepage")
# box=driver.find_element(By.ID,"hArJGc")
#box=driver.find_element(By.ID,"searchbox_input")
#box=driver.find_element(By.XPATH,"//*[@id='searchbox_homepage']")
# send_keys arayacağımız şeyi yazıyoruz.
# box.send_keys("asd")










