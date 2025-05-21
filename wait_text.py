from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math
def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

with webdriver.Chrome() as driver:
    driver.get("http://suninjuly.github.io/explicit_wait2.html")
    wait = WebDriverWait(driver, 15, poll_frequency=1)
    element = ("xpath", "//h5[@id='price']")
    wait.until(EC.text_to_be_present_in_element(element,"$100"))
    driver.find_element("xpath","//button[@id='book']").click()
    res = driver.find_element("xpath","//span[@id='input_value']").text
    driver.find_element("xpath","//input[@id='answer']").send_keys(calc(res))
    driver.find_element("xpath","//button[@type='submit']").click()
    alert = driver.switch_to.alert
    print(alert.text)
    time.sleep(15)