from selenium import webdriver
from selenium.webdriver.common.by import By
import time


with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/selenium/8/8.4.2/index.html')
    for i in range(1, 4):
        element = browser.find_element(By.ID, f'frame{i}')
        browser.switch_to.frame(element)
        browser.find_element(By.CLASS_NAME, "unlock-button").click()
        browser.switch_to.default_content()
        time.sleep(3)

    element = browser.find_element(By.ID, 'frame4')
    browser.switch_to.frame(element)
    res = browser.find_element("xpath","//h2").text
    time.sleep(3)
    print(res)

    browser.switch_to.default_content()
    browser.execute_script("return arguments[0].scrollIntoView(true);", element)
    time.sleep(3)
