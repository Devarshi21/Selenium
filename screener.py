from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
#from bse_ann import company
import time


url = "https://www.screener.in/"

service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)
driver.get(url)     # Opening the webpage

# Opening the required 
elements = driver.find_elements(By.XPATH, "//input[@type='search']")  # Returns webdriver elements
for element in elements:           #Searching for the company name
    if element.is_displayed():
        element.send_keys("Tata Motors")
        element.send_keys(Keys.ENTER)
        break




time.sleep(5)
driver.quit()