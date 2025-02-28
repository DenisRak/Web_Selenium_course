import time
from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/selenium/3/3.2.3/index.html')
    browser.find_element('xpath', '//button').click()
    r = browser.find_element(By.ID,'text1').text
    browser.find_element('xpath', '//input').send_keys(r)
    browser.find_element(By.ID, 'checkBtn').click()
    res = browser.find_element(By.ID, 'text2').text
    print(res)
    time.sleep(5)