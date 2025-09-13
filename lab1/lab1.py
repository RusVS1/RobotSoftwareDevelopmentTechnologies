from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select
import time

success = False
attempt_count = 1

while not(success):
    print("attempt", attempt_count )
    try:
        options = Options()
        options.binary_location = "/snap/bin/opera"
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--disable-gpu")
        options.add_argument("--remote-debugging-port=9222")

        service = Service("/usr/local/bin/chromedriver138")

        driver = webdriver.Chrome(service=service, options=options)
        driver.get("https://www.saucedemo.com/")
        time.sleep(3)

        login = "locked_out_user"
        backup_login = "standard_user"
        password = "secret_sauce"

        driver.find_element(By.ID, "user-name").send_keys(login)
        driver.find_element(By.ID, "password").send_keys(password)
        driver.find_element(By.ID, "login-button").click()

        time.sleep(2)
        if driver.find_element(By.CLASS_NAME, "error-button"):
            driver.find_element(By.ID, "user-name").clear()
            time.sleep(2)
            driver.find_element(By.ID, "user-name").send_keys(backup_login)
            time.sleep(2)
            driver.find_element(By.ID, "login-button").click()

        time.sleep(2)
        Select(driver.find_element(By.CLASS_NAME, "product_sort_container")).select_by_value("lohi")

        time.sleep(2)
        driver.find_element(By.CLASS_NAME, "btn_inventory").click()
        time.sleep(2)
        driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
        time.sleep(2)
        driver.find_element(By.ID, "continue-shopping").click()
        
        success = True
        print("successfully for attempts", attempt_count)

        time.sleep(10)
        driver.quit()
    except:
        driver.quit()
        attempt_count += 1