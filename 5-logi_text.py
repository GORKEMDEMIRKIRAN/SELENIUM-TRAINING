
import time as tm
from selenium import webdriver
from selenium.webdriver.edge.service import Service

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

servic=Service(".\\selenium\\msedgedriver.exe")
driver=webdriver.Edge(service=servic)

# test otomasyonu
# test: projeyi yapmadan önce beklentilerimizi karşılıyor mu 
# test mühendisleri olarak bir web sitesi bizim için 2 şey yapmalı

# 1 . istenileni yapıyor mu ?
# 2. istenmiyeni yapıyor mu ?

# bunu bir kullanıcı girişi yaptığımızı düşünelim
# yapmasını istediğimiz : kullanıcı adı ve şifre ile giriş yapması
# yapmamasını istediğimiz : yanlış kullanıcı adı ve şifre ile giriş yapması 
# Bu hatalı bir yazılım olucaktır.

# 2 şey test edicez.
# 1 .yapması gerekeni yapıyor mu ?  (pozitif test)
# 2. yapmaması gerekeni yapıyor mu ?  ( negetif test)

# ikisinide yapıyorsa yazılım başarılıdır.



# YAPILACAK İŞLEMLER

# internette login sayfasına git "https://the-internet.herokuapp.com/login"
# kullanıcı adi gir
# şifre gir
# log in düşmesine tıkla
#    yanlış kullanıcı adında      = "Your username is invalid!" hata mesajı alıyoruz.
#    yanış şifre adında           = "Your password is invalid!" hata mesajı alıyoruz.
#    kullanıcı adı ve şifre doğru = "You logged into a secure area!" mesajı alıyoruz. 
#        Başarılı girişte link değişiyor = "https://the-internet.herokuapp.com/secure"
#        Sayfadaki yazıda "SECURE AREA" olucak


driver.get("https://the-internet.herokuapp.com/login")

# KULLANICI BİLGİLERİ GİRİYOR

user_name="tomsmith"
user_password="SuperSecretPassword!"
# user_name=input("User_name: ")
# user_password=input("User_password: ")


# Kullanıcı ismi ve şifresini girirek kullanıcı giriş butonuna tıklıyor.
user_box1=driver.find_element(By.ID,"username")
user_box1.send_keys(user_name)
user_box2=driver.find_element(By.ID,"password")
user_box2.send_keys(user_password)
button=driver.find_element(By.CLASS_NAME,"radius")
button.click()

# Kullanıcı error veya girdi mesajı
user_error_message=driver.find_element(By.ID,"flash").text
# Sadece ikinci sayı değerini alır.

# 1. yöntem hata mesajındaki bir değere eşitleyerek bakıyor.
# user_error_messages=user_error_message.split(" ")[1]
# if user_error_messages=="username":
#    print("Yanlış kullanıcı adı girdiniz...")
# elif user_error_messages=="password":
#     print("Yanlış kullanıcı şifresi girdiniz....") 
# elif user_error_messages=="logged":
#     print("Başarılı giriş yaptınız...")


link=driver.current_url
# 2.yöntem hata mesajındaki bütün değerlere eşitliyor.
if "Your username is invalid!" in user_error_message:
    print("hatalı kullanıcı ismi")
elif "Your password is invalid!" in user_error_message:
    print("hatalı kullanıcı şifresi")
# elif "You logged into a secure area!" in user_error_message:   
elif "secure" in link:
    print("başarılı giriş")
    # exit_button=driver.find_element(By.CLASS_NAME,"button secondary radius").click()
    exit_button=driver.find_element(By.XPATH,"//*[@id='content']/div/a/i").click() 
# tm.sleep(100)
driver.quit()





# REFACTORING 

# yazılmış olan kodu optimize etmek.
# varolan kodu içinde falzadan olan kısımları çıkararak satır sayısını azalma 
# kodu daha anlaşılır ve etkin hale getirme


# Bu fonksiyonda sayfaya ulaşıp verilen şifre ve kullanıcı adını girerek
# çıkan mesajı döndürüyor.
def login(name,assword):
    driver.get("https://the-internet.herokuapp.com/login")
    driver.find_element(By.ID,"username").send_keys(user_name)
    driver.find_element(By.ID,"password").send_keys(user_password)
    driver.find_element(By.CLASS_NAME,"radius").click()
    message=driver.find_element(By.ID,"flash").text
    return message

print(login(user_name,user_password))


