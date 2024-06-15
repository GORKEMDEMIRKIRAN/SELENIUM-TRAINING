
# PYTHON VE SELENIUM İLE WEB TEST OTOMASYONU 

## selenium kurulum  ve web driver bağlama

from selenium import webdriver
from selenium.webdriver.chrome.service import Service


#service=Service("C:\Users\gorke\Downloads\chromedriver.exe")
#service=Service("C:\Users\gorke\Desktop\PYTHON\selenium\chromedriver.exe")

# 2 türlüde açıyor selenium dosya içindeki cromedriver ya da indirilenlerdeki cromedriver
service=Service(".\\selenium\\chromedriver.exe")
#service=Service("C:\\Users\\gorke\\Downloads\\chromedriver.exe")

drivers=webdriver.Chrome(service=service)
drivers.get("https://www.apple.com")





## INTERNET TARAYICI İLE TEMEL FONKSİYONLAR

# güncel url linkini aldık.
link=drivers.current_url
baslik=drivers.title
print("sayfa başlığı: "+baslik)

if "apple.com" in link:
    print("Doğru apple sayfasındayız: "+link)
drivers.get("http://www.etsy.com")


# ekranı büyültmek için
drivers.maximize_window()


link=drivers.current_url
baslik=drivers.title
print("sayfa başlığı: "+baslik)

if "etsy.com" in link:
    print("Doğru etsy sayfasındayız: "+link)



# sayfada geri gitme
drivers.back()
# sayfasımızın doğru yere gittiğin görmek için
baslik=drivers.title

#drivers.save_screenshot(".\\selenium\\screenshot.png")

if "Apple" in baslik:
    print("Tebrikler")
else:
    # başlıkta apple yoksa biz istediğimiz sayfayaa gitmedik.
    # bunun için ekran görüntüsü(screenshot) alıcaz.
    drivers.save_screenshot(".\\selenium")
    



import time
time.sleep()




# suan ki pencereyi kapatıcak.
# drivers.close()

# selenium kullandığı tüm pencereleri kapatıcak.
# selenium aynı anda bir kaç sekmeyi yönetemiyor.
# örneğin yeni bir sekme açtımı selenium sadece birini kullanıyor
# ama bu kod bütün pencereleri kapatık.
# drivers.close ise sadece bulunduğu pencereyi kapatır.
drivers.quit()



# # sayfada ileri gitme
# drivers.forward
# # sayfayı yenileme
# drivers.refresh




















