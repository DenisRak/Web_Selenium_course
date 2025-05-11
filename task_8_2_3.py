import time
from selenium.webdriver.support import expected_conditions as EC

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/selenium/8/8.2.1/index.html')
    time.sleep(2)
    browser.set_window_size(1200, 720)
    browser.find_element(By.ID, "checkSizeBtn").click()

    secret = WebDriverWait(browser, 5).until(EC.visibility_of_element_located((By.ID, 'secret'))).text
    print(secret)
    time.sleep(3)