import time
from selenium import webdriver
from selenium.webdriver.common.by import By
counter = 0
with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/selenium/3/3.3.3/index.html')
    lst = browser.find_elements('xpath', '//a')
    time.sleep(2)
    for el in lst:
        x = el.get_attribute('stormtrooper')
        if x.isdigit():
            counter += int(x)
    browser.find_element('xpath', '//input').send_keys(str(counter))
    time.sleep(2)
    browser.find_element(By.ID, 'checkBtn').click()
    res = browser.find_element(By.ID, 'feedbackMessage').text
    print(res)
    time.sleep(5)



