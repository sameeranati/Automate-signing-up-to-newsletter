from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
chrome_driver_path="C:\development\chromedriver.exe"
options = webdriver.ChromeOptions()
driver=webdriver.Chrome(service=Service(chrome_driver_path),options=options)

def browser_function():
    driver.get("https://web.archive.org/web/20220120120408/https://secure-retreat-92358.herokuapp.com/")
    first_name=driver.find_element(By.CSS_SELECTOR,'body > form > input.form-control.top')
    first_name.send_keys("sameera")
    last_name=driver.find_element(By.CSS_SELECTOR,'body > form > input.form-control.middle')
    last_name.send_keys("nati")
    email=driver.find_element(By.CSS_SELECTOR,'body > form > input.form-control.bottom')
    email.send_keys("sameeranati@gmail.com")
    signup=driver.find_element(By.CSS_SELECTOR,'body > form > button')
    signup.send_keys(Keys.ENTER)
    while True:
        pass

browser_function()
