from selenium import webdriver
from selenium.webdriver.common.by import By
import re

with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/selenium/8/8.4.1/')
    element = browser.find_element(By.TAG_NAME, 'iframe')
    browser.switch_to.frame(element)
    content = browser.page_source
    res = re.findall(r'(?<=\*)\w+(?=\*)', content)

    print(''.join(res))