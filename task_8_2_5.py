import time
from selenium.webdriver.support import expected_conditions as EC

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/selenium/8/8.2.2/index.html')
    time.sleep(2)
    out = sum(browser.get_window_size().values())
    browser.find_element(By.ID, "answer").send_keys(out)
    browser.find_element(By.ID, "checkBtn").click()
    result = WebDriverWait(browser, 5).until(EC.visibility_of_element_located((By.ID, 'resultMessage')))
    print(result.text)
    time.sleep(3)