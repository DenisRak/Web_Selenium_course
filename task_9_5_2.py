from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time


with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/selenium/9/9.5.1/index.html')
    result = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.ID, "order-number")))
    print(result.text)
    time.sleep(5)