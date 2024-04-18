import time
from selenium import webdriver
from selenium.webdriver.common.by import By

data = ['John', 'Snow', 'Bill', '38', 'Colorado', 'JS_americ@gmail.com']

with webdriver.Chrome() as driver:
    driver.get('http://parsinger.ru/selenium/1/1.html')

    elements = driver.find_elements("xpath", "//input[@class='form']")
    for i, el in enumerate(elements):
        el.send_keys(data[i])
    driver.find_element("xpath","//input[@type='button']").click()
    result = driver.find_element("xpath","//span[@id='result']")
    time.sleep(3)
    print(result.text)
