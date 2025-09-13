from selenium import webdriver
from selenium.webdriver.chrome.options import Options

opera_path = "C:\Users\russm\AppData\Local\Programs\Opera"

options = Options()
options.binary_location = opera_path

url = "https://www.saucedemo.com/"

driver = webdriver.Chrome(options=options)
driver.get(url)