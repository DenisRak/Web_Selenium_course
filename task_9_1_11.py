'''Задание:
Мир Цветов: Войдите на указанный сайт с помощью Selenium, где вас встретят яркие, цветные шарики, каждый из которых ждёт своей очереди,
чтобы оказаться в своём уютном контейнере.
Задача Сортировки: Ваша миссия - написать скрипт, который поможет каждому шарику найти его дом, соответствующий по цвету блок.
Используйте свои знания и умения, чтобы аккуратно и внимательно перенести каждый шарик в его контейнер.
Секретное Сообщение: Как только последний шарик опустится в свой блок, на сцене появится секретное сообщение.
Это сообщение - символ вашей победы, вашего умения создавать порядок из хаоса и находить гармонию в мире цветов.'''



import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.color import Color

url = "https://parsinger.ru/selenium/5.10/4/index.html"

options = webdriver.ChromeOptions()
options.add_argument("--incognito")
options.add_argument("--window-size=1280,800")

with webdriver.Chrome(options=options) as driver:
    action = ActionChains(driver)
    driver.get(url)
    time.sleep(2)
    lst = driver.find_elements("xpath","//div[contains(@class,'basket_color')]")
    bolls = driver.find_elements("xpath","//div[contains(@class,'ball_color')]")
    for el in lst:
        col = Color.from_string(el.value_of_css_property('background-color'))
        for bol in bolls:
            if col == Color.from_string(bol.value_of_css_property('background-color')):
                action.drag_and_drop(bol, el).perform()
                time.sleep(1)

    res = driver.find_element("xpath","//p[@class='message']")
    print(res.text)
