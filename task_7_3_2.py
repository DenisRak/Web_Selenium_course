""" Задача: помогите Питеру Гриффину добраться до бассейна, термометр показывает +35🌡️."""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

with (webdriver.Chrome() as browser):
    browser.get(r"http://parsinger.ru/selenium/7/7.3.1/index.html")
    actions = ActionChains(browser)
    draggable = browser.find_element(By.ID, "draggable")
    target = browser.find_element(By.ID, "target")
    actions.drag_and_drop(draggable, target).perform()
    time.sleep(1)
    result = browser.find_element(By.ID, "password")
    print(result.text)