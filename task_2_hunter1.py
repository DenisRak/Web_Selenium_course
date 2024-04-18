from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

with webdriver.Chrome(service=Service(ChromeDriverManager().install())) as driver:
    driver.get("http://parsinger.ru/selenium/2/2.html")
    driver.find_element(By.LINK_TEXT, "16243162441624").click()
    res = driver.find_element("xpath","//p[@id='result']")
    time.sleep(3)
    print(res.text)