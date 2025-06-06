from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time
import re

with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/selenium/9/9.4.2/index.html')
    previous_url = browser.current_url
    time.sleep(3)
    browser.find_element(By.CLASS_NAME, "button-text").click()
    cnt = 0
    WebDriverWait(browser, 5).until(EC.url_changes(previous_url))
    while True:
        try:
            current_url = browser.current_url
            if re.match(r'^https://parsinger\.ru/selenium/9/9\.4\.2/ok/ok_\d+\.html$', current_url):
                number = WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.CLASS_NAME, "number"))).text
                cnt += int(number)
            WebDriverWait(browser, 5).until(EC.url_changes(current_url))
        except TimeoutException:
            break
    if "index_2" in browser.current_url:
        browser.find_element(By.ID, "sumInput").send_keys(str(cnt))
        browser.find_element(By.ID, "checkButton").click()
        print(browser.find_element(By.ID, 'result').text)
    time.sleep(3)
