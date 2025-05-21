import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/selenium/9/9.1.1/index.html')
    for i in range(1, 5):
        WebDriverWait(browser, 10 + i).until(EC.element_to_be_clickable((By.ID, f"button{i}"))).click()

    WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.ID, "finalButton"))).click()
    secret = WebDriverWait(browser, 5).until(EC.visibility_of_element_located((By.ID, "message")))
    print(secret.text)
    time.sleep(3)