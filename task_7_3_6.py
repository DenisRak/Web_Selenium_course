"""Задача: нажмите комбинацию клавиш CTRL + ALT + SHIFT + T, чтобы получить секретный пароль."""


from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

with webdriver.Chrome() as browser:
    browser.get(r"https://parsinger.ru/selenium/7/7.3.3/index.html")
    actions = ActionChains(browser)
    element = browser.find_element(By.ID,"instructions")
    time.sleep(2)
    actions.key_down(Keys.CONTROL, element).key_down(Keys.ALT).key_down(Keys.SHIFT).key_down('T').perform()
    time.sleep(2)
    actions.key_up(Keys.CONTROL).key_up(Keys.ALT).key_up(Keys.SHIFT).key_up('T').perform()
    time.sleep(2)
    result = browser.find_element("xpath","//*[@key='access_code']")
    print(result.text)







