from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time
from selenium.webdriver.common.by import By


with webdriver.Chrome() as driver:
    driver.get('https://parsinger.ru/selenium/5.10/8/index.html')
    time.sleep(2)
    pieces = driver.find_elements(By.CLASS_NAME, "piece")
    gryds = driver.find_elements(By.CLASS_NAME, "range")
    action = ActionChains(driver)
    for p,g  in zip(pieces, gryds):

        action.drag_and_drop(p,g).perform()
    time.sleep(5)
    res = driver.find_element(By.ID, 'message')
    print(res.text)
