
# DROPDOWN LİSTELER TIKLADIĞIMIZDA AÇILAN LİSTELER


# Bunu statik dropdown olarak anlatılmıştır.
# Birde dinamik dropdown var.

# STATIK DROPDOWN

# Tıkladığımızda alt alta bilgilerin çıktığı bilgilerdir.
# Statik olması sayfa açıkken altta yazan bilgilerin görünmemesidir.
# tıkladıktan sonra görünen bilgilerdir.


import time as tm
from selenium import webdriver
from selenium.webdriver.edge.service import Service as sv_edge
from selenium.webdriver.chrome.service import Service as sv_chrome

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

# servic_edge=sv_edge(".\\selenium\\msedgedriver.exe")
# driver_edge=webdriver.Edge(service=servic_edge)
# driver_edge.get("https://tomspizzeria.b4a.app")


servic_chrome=sv_chrome(".\\chromedriver.exe")
driver_chrome=webdriver.Chrome(service=servic_chrome)
driver_chrome.get("https://tomspizzeria.b4a.app")

# dropdown için bir class oluşturulmuş
# "select" class import edip kullanıcaz.

from selenium.webdriver.support.ui import Select

# ödeme tipine tıkladık.
dropdown=driver_chrome.find_element(By.ID,"odeme-tipi")
# şimdi selenium hangi elementin dropdown olduğunu söylememiz lazım.
payment=Select(dropdown)

payment_types=payment.options
for types in payment_types:
    print(types.text)
    
payment.select_by_visible_text("Nakit")


# payment. yazılan fonksiyonlar 
#   .options()                 fonksiyonu = ödeme dropdown altındaki seçenekleri vericektir.
#                                          Bunu bir listeye koyabilirim.
#   .select_by_visible_text() fonksiyonu = Benim verdiğim "text" olan seçeneği seçicektir.
#   .select_by_index()        fonksiyonu = index olarak opsiyonu seçiyoruz.(unutma 0.index başlıyor.)
#   .first_seşected_option()  fonksiyonu = Birden fazla seçenek var ise ilk seçiyor.
#   .is_multiple()            fonksiyonu = Birden fazla dropdown ise ona göre true,false veriyor.
#   .all_selected_options()   fonksiyonu = birden fazla opsiyon seçili ise onların listesini veriyor.
#   .deselect_by_index()      fonksiyonu = kaldırmak istedğinizin index görebilirsiniz.

tm.sleep(20)
