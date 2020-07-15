from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Firefox()
driver.get("https://humanbenchmark.com/tests/memory")


while True:
    element = WebDriverWait(driver, 100, poll_frequency=0.001).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".square.active"))
    )
    newboxes = [
        element for element in driver.find_elements_by_css_selector(".square.active")
    ]
    # notfound = True
    # while notfound:
    #     newboxes = [
    #         element
    #         for element in driver.find_elements_by_class_name("active")
    #     ]
    #     notfound = len(newboxes) <= 1
    time.sleep(2)
    for element in newboxes:
        element.click()
    time.sleep(1)
