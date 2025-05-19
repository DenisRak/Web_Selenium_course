import time
from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/selenium/8/8.3.1/index.html')
    browser.find_element(By.ID, 'alertButton').click()
    browser.switch_to.alert.accept()
    time.sleep(2)
    browser.find_element(By.ID, 'promptButton').click()
    time.sleep(1)
    browser.switch_to.alert.send_keys('Alert')
    browser.switch_to.alert.accept()
    browser.find_element(By.ID, 'confirmButton').click()
    time.sleep(1)
    browser.switch_to.alert.accept()
    pswd = browser.find_element(By.ID, 'secretKey').text
    print(pswd)
