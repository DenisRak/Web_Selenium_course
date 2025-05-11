import time
from selenium import webdriver
from selenium.webdriver.common.by import By


with webdriver.Chrome() as browser:
    browser.get("https://parsinger.ru/selenium/8/8.1.2/index.html")

    input_field = browser.find_element(By.ID, "sumInput")
    button = browser.find_element(By.ID, "checkButton")
    links = browser.find_elements(By.TAG_NAME, "a")
    home_page = browser.current_window_handle

    total = 0
    for link in links:
        url = link.get_attribute("href")
        browser.switch_to.new_window('tab')
        browser.get(url=url)
        time.sleep(5)

        numbers = browser.find_elements(By.CLASS_NAME, "number")
        total += sum(int(number.text) for number in numbers)

        browser.switch_to.window(home_page)

    input_field.send_keys(total)
    button.click()

    password = browser.find_element(By.ID, "passwordDisplay").text
    print(password)