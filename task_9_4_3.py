from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time

with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/selenium/9/9.4.3/index.html')
    browser.find_element(By.XPATH, '//a[text()="Правильный путь"]').click()
    WebDriverWait(browser, 10).until(EC.url_to_be("https://parsinger.ru/selenium/9/9.4.3/final.html?key=secure"))
    password = browser.find_element(By.ID, "password").text
    print(password)
    time.sleep(3)