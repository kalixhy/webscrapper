from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions  as EC

service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)

#enter url to search for
driver.get("https://google.com")

WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.CLASS_NAME, "gLFyf" ))
)

input_element = driver.find_element(By.CLASS_NAME, "gLFyf")
#enter what you want to search for
input_element.clear()
input_element.send_keys("global football awards" + Keys.ENTER)

WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.CLASS_NAME, "gLFyf" ))
)

link = driver.find_element(By.PARTIAL_LINK_TEXT, "global football awards")
link.click()




time.sleep(10)
driver.quit



