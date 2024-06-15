
import time as tm
from selenium import webdriver
from selenium.webdriver.edge.service import Service

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

servic=Service(".\\selenium\\msedgedriver.exe")
driver=webdriver.Edge(service=servic)

user_name="tomsmith"
user_password="SuperSecretPassword!"

def login(name,assword):
    driver.get("https://the-internet.herokuapp.com/login")
    driver.find_element(By.ID,"username").send_keys(user_name)
    driver.find_element(By.ID,"password").send_keys(user_password)
    driver.find_element(By.CLASS_NAME,"radius").click()
    message=driver.find_element(By.ID,"flash").text
    return message

link=driver.current_url
user_error_message=login(user_name,user_password)
if "Your username is invalid!" in user_error_message:
    print("hatalı kullanıcı ismi")
elif "Your password is invalid!" in user_error_message:
    print("hatalı kullanıcı şifresi") 
elif "secure" in link:
    exit_button=driver.find_element(By.XPATH,"//*[@id='content']/div/a/i").click() 
# tm.sleep(10)
driver.quit()

