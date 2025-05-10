from selenium import webdriver
import time
import re

with webdriver.Chrome() as browser:
    browser.get("about:blank")
    time.sleep(2)
    browser.switch_to.new_window("tab")
    browser.get("https://parsinger.ru/selenium/8/8.1/site1/")
    num1 = re.sub(r"[439]", "", browser.title)
    time.sleep(2)
    browser.switch_to.new_window("tab")
    browser.get("https://parsinger.ru/selenium/8/8.1/site2/")
    num2 = re.sub(r"[780]", "", browser.title)

    time.sleep(2)
    print(int(num1) + int(num2))
