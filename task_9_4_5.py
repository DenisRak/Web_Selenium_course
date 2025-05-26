from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time

with webdriver.Chrome() as browser:
    browser.get('http://parsinger.ru/selenium/9/9.4.1/3VT6JyXnI7EQqG0632xSAQyD4Z.html')
    while True:
        try:
            WebDriverWait(browser, 5).until(EC.url_contains("qLChv49"))
            browser.find_element(By.ID, "checkButton").click()
            result = browser.find_element("xpath", "//p").text
            print(result)
            break
        except TimeoutException:
            browser.find_element(By.ID, "searchLink").click()
