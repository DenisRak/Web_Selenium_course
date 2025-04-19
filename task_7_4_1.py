from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import time

with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/selenium/7/7.4.1/index.html')
    time.sleep(3)
    div = browser.find_element(By.CLASS_NAME, "long-page")
    ActionChains(browser).move_to_element(div).scroll_by_amount(0, 700).perform()
    time.sleep(5)
    res = browser.find_element(By.CLASS_NAME, "step-content").text
    ActionChains(browser).move_to_element(div).scroll_by_amount(0, 1400).perform()
    time.sleep(5)
    browser.find_element("xpath", '//input').send_keys(res.split()[-1])
    browser.find_element("xpath", "//button").click()
    time.sleep(5)
    key = browser.find_element(By.ID, "final-key")

    print(key.text)