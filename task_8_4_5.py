from selenium import webdriver
from selenium.webdriver.common.by import By
import time


with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/selenium/8/8.4.3/index.html')
    for _ in range(4):
        element = browser.find_element(By.TAG_NAME, 'iframe')
        browser.switch_to.frame(element)
        browser.find_element(By.CLASS_NAME, "button").click()
        time.sleep(3)
    res = browser.find_element(By.CLASS_NAME, "password-container")
    print(res.text)
    time.sleep(1)