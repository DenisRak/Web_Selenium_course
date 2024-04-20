""" Посетить указанный веб-сайт, систематически пройти по всем категориям, страницам
 и карточкам товаров (всего 160 шт.). Из каждой карточки товара извлечь стоимость и
  умножить ее на количество товара в наличии. Полученные значения агрегировать
  для вычисления общей стоимости всех товаров на сайте."""

import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


with webdriver.Chrome(service=Service(ChromeDriverManager().install())) as driver:
    total = 0
    for i in range(1, 6):
        for j in range(1, 5):
            driver.get(f"http://parsinger.ru/html/index{i}_page_{j}.html")
            lst = driver.find_elements("class name", "name_item")

            urls = [el.get_attribute('href') for el in lst]
            for el in urls:
                driver.get(el)
                count = int(driver.find_element("id","in_stock").text.split()[-1])
                price = int(driver.find_element("id","price").text.split()[0])
                total += (count * price)
    print(total)