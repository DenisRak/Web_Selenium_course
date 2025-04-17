import time
from selenium.webdriver import Keys
from selenium import webdriver
from selenium.webdriver.common.by import By


with (webdriver.Chrome() as browser):
    browser.get(r"https://parsinger.ru/selenium/7/7.2/index.html")
    lst = []
    while True:
        input_tags = browser.find_elements(By.TAG_NAME, 'input')
        for tag_input in input_tags:
            if tag_input not in lst:
                tag_input.send_keys('fuckoff', Keys.ENTER, Keys.ARROW_DOWN)
                time.sleep(0.5)
                lst.append(tag_input)

        if len(lst) == 100:
            break


    res = browser.find_element(By.ID, 'hidden-password')
    print(res.text)


