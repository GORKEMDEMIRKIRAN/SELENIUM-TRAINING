

# RADYO DÜĞMESİ CHECKBOX

# radyo düğmesi seçeneklerin yanında nokta işaretli seçim yöntemidir.


import time as tm
from selenium import webdriver
from selenium.webdriver.edge.service import Service as sv_edge
from selenium.webdriver.chrome.service import Service as sv_chrome

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions



# EDGE SAYFA AÇMA

# servic_edge=sv_edge(".\\selenium\\msedgedriver.exe")
# driver_edge=webdriver.Edge(service=servic_edge)
# driver_edge.get("https://tomspizzeria.b4a.app")

# CHROME SAYFA AÇMA

servic_chrome=sv_chrome(".\\selenium\\chromedriver.exe")
driver_chrome=webdriver.Chrome(service=servic_chrome)
driver_chrome.get("https://tomspizzeria.b4a.app")



# 3 farklı clickleme yöntemleride var onlarıda öğrenelim.

# is_displayed = bool bir değer döndürür Ture,false şeklinde(eğer tıklarsa TRUE, diğler durumda FALSE)
# is_enabled   = bir butona tıklama açık olup olmadığına bakabiliyoruz (True,false)
# is_selected  = seçili olup olmadığını çevirir.(true,false)

# 1. is_selected() şayet web element seçili ise True , aksi halde değilse False verecektir. 
# 2. is_displayed() şayet web element sayfada kullanıcıya görünür durumda ise True, aksi halde False verecektir. 
# 3. is_enabled() ise web element kullanıcının etkileşimine açıksa True, aksi halde False verecektir.



orta_boy=driver_chrome.find_element(By.CSS_SELECTOR,"input[value='Orta']")
zeytin=driver_chrome.find_element(By.CSS_SELECTOR,"input[value='zeytin']")
mantar=driver_chrome.find_element(By.CSS_SELECTOR,"input[value='mantar']")

print(orta_boy.is_selected())
print(zeytin.is_selected())
print(mantar.is_selected())

orta_boy.click()
zeytin.click()
mantar.click()

print(orta_boy.is_selected())
print(zeytin.is_selected())
print(mantar.is_selected())

tm.sleep(20)









