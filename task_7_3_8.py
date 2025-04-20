from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

with webdriver.Chrome() as browser:
    browser.get("https://parsinger.ru/selenium/7/7.3.5/index.html")
    actions = ActionChains(browser)
    el1 = browser.find_element(By.ID,"scrollable-container-left")
    actions.click(el1).send_keys(Keys.END).perform()
    el2 = browser.find_element(By.ID, "scrollable-container-right")
    actions.click(el2).send_keys(Keys.END).perform()
    time.sleep(3)
    res = browser.find_element(By.CSS_SELECTOR, '[key="access_code"]')
    print(res.text)

