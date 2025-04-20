from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
import time
with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/selenium/7/7.5/index.html')
    container = browser.find_element(By.ID, 'container')
    elements = []
    total = 0
    while True:
        divs = [x for x in browser.find_elements(By.CLASS_NAME, 'card')]
        for div in divs:
            if div not in elements:
                div.find_element(By.CLASS_NAME, 'like-btn').click()
                total += int(div.find_element(By.CLASS_NAME, 'big-number').text)
                elements.append(div)
        if len(elements) == 100:
            break
        container.send_keys(Keys.ARROW_DOWN)
        time.sleep(1)
print(total)