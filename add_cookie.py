import time
from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/selenium/6/6.3.3/index.html')
    dct = {'name': 'secretKey', 'value': 'selenium123'}
    browser.add_cookie(dct)
    browser.refresh()
    time.sleep(5)
    res = browser.find_element(By.ID,'password')
    print(res.text)


