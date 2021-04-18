from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from credentials import insta_username,insta_password

chromePath="D:\Visual studio\python\JARVIS\chromedriver.exe"
drv=webdriver.Chrome(executable_path=chromePath)

drv.get('https://www.instagram.com/accounts/login/?source=auth_switcher')
time.sleep(5)
drv.find_element_by_name("username").send_keys(insta_username)
drv.find_element_by_name("password").send_keys(insta_password) 
drv.find_element_by_name("password").send_keys(u'\ue007')
print("Yor are succesfully logged in...")