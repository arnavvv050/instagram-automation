import selenium
from selenium import webdriver

import time

from selenium.webdriver import Keys
from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from webdriver_manager.chrome import ChromeDriverManager

browser = webdriver.Chrome(ChromeDriverManager().install())
time.sleep(1)
browser.get("https://www.instagram.com")
time.sleep(4)
# login

Username = browser.find_element('xpath', '//*[@id="loginForm"]/div/div[1]/div/label/input')
#enter ur username
Username.send_keys("")
time.sleep(4)
#enterpassword
Password = browser.find_element('xpath', '//*[@id="loginForm"]/div/div[2]/div/label/input')
Password.send_keys("//")
Password.submit()
time.sleep(3)

# not now
Notnow = browser.find_element('xpath','/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/section/main/div/div/div/div/button')
time.sleep(4)

# notification
Noti = browser.find_element('xpath',"/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]")
Noti.click()
time.sleep(4)
def firstpic():
    time.sleep(2)
    pic = browser.find_element('class_name',"_aagw")
    pic.click()

def likepic():
    time.sleep(4)
    like =browser.find_element('xpath','/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/section/main/div[1]/section/div/div[2]/div[1]/div/article[1]/div/div[3]/div/div/section/span[1]/button/div[1]/svg')
    like.click()

firstpic()
likepic()
