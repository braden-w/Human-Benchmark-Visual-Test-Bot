from selenium import webdriver
import time

driver = webdriver.Firefox()
driver.get("https://humanbenchmark.com/tests/memory")


try:
    while True:
        notfound = True
        while notfound:
            newboxes = [
                element
                for element in driver.find_elements_by_class_name("active")
            ]
            notfound = len(newboxes) == 0
        # time.sleep(3)
        # for element in newboxes:
        #     try:
        #         element.click()
        #     except:
        #         continue
        
finally:
    driver.quit
