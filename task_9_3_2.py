"""Неявное ожидание"""

import time
from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as browser:
    browser.implicitly_wait(6)
    browser.get('http://parsinger.ru/selenium/9/9.3.1/index.html')
    browser.find_element(By.ID, 'startButton').click()
    time.sleep(3)
    for _ in range(5):
        browser.find_element(By.ID, 'dynamicButton').click()
    time.sleep(2)
    res = browser.find_element(By.ID, 'secretPassword')
    print(res.text)

