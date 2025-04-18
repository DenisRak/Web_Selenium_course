from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

with (webdriver.Chrome() as browser):
    browser.get(r"https://parsinger.ru/selenium/7/7.3.2/index.html")
    actions = ActionChains(browser)
    element = browser.find_element(By.ID, "dblclick-area")
    actions.double_click(element).perform()
    password = browser.find_element(By.ID, "password")
    print(password.text)
    time.sleep(3)