from selenium import webdriver
import time
from cookies_list import cookies

url = 'https://parsinger.ru/selenium/5.6/1/index.html'
with webdriver.Chrome() as driver:
    driver.get(url)
    time.sleep(3)
    res = []
    for el in cookies:
        driver.add_cookie(el)
        driver.refresh()
        time.sleep(1)

        age = driver.find_element("xpath","//span[@id='age']")
        a,b = age.text.split()
        skills = driver.find_elements("xpath","//ul[@id='skillsList']/li")
        for cookie in driver.get_cookies():
            val = cookie['value']
        res.append((int(b), len(skills), val))
        driver.delete_all_cookies()

out = max(res, key=lambda x: (-x[0],x[1]))
print(out)

