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

name = ["Josts Engineering Company Ltd"]
def screener(company_name):
    url = "https://www.screener.in/"

    service = Service(executable_path="chromedriver.exe")
    driver = webdriver.Chrome(service=service)
    driver.get(url)     # Opening the webpage

    # Opening the required 
    elements = driver.find_elements(By.XPATH, "//input[@type='search']")  # Returns webdriver elements
    for element in elements:           #Searching for the company name
        if element.is_displayed():
            element.send_keys(company_name)
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, "dropdown-content"))
            )
            element.send_keys(Keys.RETURN)
            break

    market_value = driver.find_element(By.CLASS_NAME, "number").text
    company_value = (market_value + "Cr")  # Printing the market cap of the company
    print(f"Market Cap of {company_name} is : {company_value}")
    driver.quit()
    return company_value

screener(name[0].split(' ')[0] + " " + name[0].split(' ')[1])