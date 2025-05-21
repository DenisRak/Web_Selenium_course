from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time

with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/selenium/9/9.2.1/index.html')
    browser.find_element(By.ID, "startScan").click()
    time.sleep(1)
    element = WebDriverWait(browser, 30).until(EC.title_is('Access Granted'))
    time.sleep(2)
    res = browser.find_element(By.CLASS_NAME, "highlight").text

    print(res)