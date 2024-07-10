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