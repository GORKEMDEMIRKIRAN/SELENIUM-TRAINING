

from selenium import webdriver
from selenium.webdriver.edge.service import Service

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

servic=Service(".\\msedgedriver.exe")
driver=webdriver.Edge(service=servic)

driver.get("https://tr.wikipedia.org/wiki/Anasayfa")

write_Cell=driver.find_element(By.ID,"mp-tfa")
write_text=write_Cell.text
print(write_text)

write_text=write_text.split(",")[0]
print(write_text)

 
day_maddesi=driver.find_element(By.ID,"mf-tfp").text
madde=day_maddesi.split(",")[0]
print(madde)


