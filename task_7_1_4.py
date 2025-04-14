""" Задача: с помощью Selenium выполните прокрутку страницы."""

import time
from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/selenium/7/7.1/index.html')
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(5)
    res = browser.find_element(By.ID, 'secret-container')
    print(res.text)


