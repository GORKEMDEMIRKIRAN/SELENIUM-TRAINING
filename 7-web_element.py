
# WEB ELEMENT LİSTESİ

# "https://www.imdb.com/"

# //span[text()="metin yazısı"]
# td =tablo demektir.


# find_element= verdiğimiz ilk sorguya uyan elementi veriyor.
# find_elements = o sorguya uyan kaç tane element varsa liste halinde veriyor.

import time as tm
from selenium import webdriver
from selenium.webdriver.edge.service import Service

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

servic=Service(".\\selenium\\msedgedriver.exe")
driver=webdriver.Edge(service=servic)
driver.get("https://www.imdb.com/")


driver.find_element(By.ID,"imdbHeader-navDrawerOpen").click()
# driver.find_element(By.XPATH,"//span[text()='Movies']").click()
# driver.find_element(By.XPATH,"//span[text()='Top 250 Movies']").click()
driver.save_screenshot(".\\selenium\\as.png")
# film_names=driver.find_elements(By.XPATH,"//data-testid//ul//li[@class='ipc-metadata-list-summary-item__c']")

# for i in range(20):
#     print(film_names[i].text)
tm.sleep(100)


