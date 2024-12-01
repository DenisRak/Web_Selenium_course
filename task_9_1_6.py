import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

url = "https://parsinger.ru/selenium/5.10/3/index.html"

with webdriver.Chrome() as driver:
    action = ActionChains(driver)
    driver.get(url)
    time.sleep(2)
    element = driver.find_elements("class name","draganddrop")
    target = driver.find_elements("class name", "draganddrop_end")
    for i, j in zip(element, target):
        action.drag_and_drop(i, j).perform()
        time.sleep(1)
    res = driver.find_element("xpath","//p[@id='message']")
    print(res.text)