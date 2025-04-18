from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

with webdriver.Chrome() as browser:
    browser.get(r"https://parsinger.ru/selenium/7/7.3.4/index.html")
    actions = ActionChains(browser)
    element = browser.find_element(By.ID,"context-area")
    actions.context_click(element).perform()
    time.sleep(3)
    browser.find_element(By.CSS_SELECTOR,"[data-action='get_password']").click()
    time.sleep(5)
    result = browser.find_element(By.CSS_SELECTOR, "[key='access_code']")
    print(result.text)
