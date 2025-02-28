import time
from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/selenium/6/6.2/index.html')
    browser.find_element('xpath', '//a').click()
    time.sleep(2)
    browser.find_element('xpath', '//a').click()
    browser.back()
    browser.back()
    browser.find_element('xpath', '//button').click()
    print(browser.switch_to.alert.text)

    time.sleep(5)