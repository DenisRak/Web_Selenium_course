"""1️⃣ Откройте сайт-тренажёр с помощью Selenium.
2️⃣ Прокрутите страницу вниз до кнопки "Финиш!". Используйте scrollIntoView()метод прокрутки к элементу с id="target".
3️⃣ Нажмите на кнопку "Финиш!".
4️⃣ Извлеките секретный ключ."""


import time
from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/selenium/6/6.5/index.html')
    element = browser.find_element(By.ID, 'target')
    time.sleep(2)
    browser.execute_script("return arguments[0].scrollIntoView(true);", element)
    element.click()
    print(browser.find_element(By.ID, "secret-key").text)
    time.sleep(5)