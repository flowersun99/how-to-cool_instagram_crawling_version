import requests
from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys
from selenium import webdriver as wd
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import re
import pandas as pd
import numpy as np


# pre information 
username = #write your instagram id
userpw = #write your instagram password
time.sleep(3)


# your goal url 값
url = 'https://www.instagram.com/kittybunnypony/?igshid=YmMyMTA2M2Y%3D' #this is my friend's page so, click like and write command!


# login URL
loginUrl = 'https://www.instagram.com/accounts/login/'

# Chrome drvier 실행
driver = wd.Edge("C:/Users/jean8/OneDrive/바탕 화면/python workspace/msedgedriver") # write your msedgedriver's path
driver.maximize_window()
driver.get(loginUrl)
time.sleep(3)

# login
driver.find_element(By.NAME, 'username').send_keys(username)
driver.find_element(By.NAME, 'password').send_keys(userpw)
time.sleep(2)
driver.find_element(By.CSS_SELECTOR, 'button.sqdOP.L3NKy.y3zKF').click()
time.sleep(5)

driver.get(url)
time.sleep(3)

driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.PAGE_DOWN)
time.sleep(2)
# click first posting
driver.find_element(By.CSS_SELECTOR, 'div._aabd._aa8k._aanf').click()
time.sleep(3)

for i in range(200):     
    # to click next posting
    driver.find_element(By.CSS_SELECTOR, 'div._aaqg._aaqh').click()
    time.sleep(3)
