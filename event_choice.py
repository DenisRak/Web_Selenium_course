import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

url = "https://parsinger.ru/selenium/5.7/4/index.html"

with webdriver.Chrome() as driver:
    action = ActionChains(driver)
    wait = WebDriverWait(driver, 30, poll_frequency=1)
    driver.get(url)
    time.sleep(3)
    div = driver.find_element("xpath","//div[@id='main_container']/div")

    alert = ("class name","alert_button")
    flag = True
    out = []
    while flag:
        checks = [x for x in driver.find_elements("xpath","//input")]
        for el in checks:
            if el not in out:
                if int(el.get_attribute("value"))%2==0:
                    el.click()
                out.append(el)
                driver.execute_script("return arguments[0].scrollIntoView(true);", el)
            if len(out) == 1000:
                flag = False
        #action.move_to_element(div).scroll_by_amount(0, 10000).perform()
    if driver.find_element(*alert).is_displayed():
        driver.find_element(*alert).click()
        print(driver.switch_to.alert.text)

        time.sleep(2)


        #a = wait.until(EC.visibility_of_element_located(alert))
        #a.click()
        #flag = False