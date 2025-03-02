import time
from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/selenium/3/3.3.1/index.html')
    browser.find_element(By.ID, 'parent_id').find_element(By.CLASS_NAME, 'child_class').click()
    res = browser.find_element(By.ID, 'parent_id').find_element(By.CLASS_NAME, 'child_class').get_attribute('password')
    print(res)
    time.sleep(5)