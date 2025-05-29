from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

company = []
def scrapper():

    url = "https://www.bseindia.com/corporates/ann.html"

    service = Service(executable_path="chromedriver.exe")
    driver = webdriver.Chrome(service=service)

    driver.get(url)     # Opening the webpage

    # Selecting the first option from the dropdown menu
    first_dropdown = Select(WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "ddlPeriod"))
    ))
    first_dropdown.select_by_value("Company Update")    ### Change this to "Company Update" when done
    # Wait till first dropdown is registered
    # Then selecting the option from the second dropdown
    #time.sleep(2)
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "subcat"))
    )

    dropdown_element2 = driver.find_element(By.NAME, "subcat")
    select2 = Select(dropdown_element2)

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//select[@id='ddlsubcat']/option[text()='Allotment of Warrants']"))
    )
    select2.select_by_visible_text("Award of Order / Receipt of Order")   ### Change this to "Award of Order / Receipt of Order" when done

    # Clicking the submit button

    button_element = driver.find_element(By.NAME, "submit") 
    button_element.send_keys(Keys.ENTER)


    # Extracting the name/s of companies
    WebDriverWait(driver, 1).until(
        EC.presence_of_element_located((By.XPATH, "//span[@ng-bind-html='cann.NEWSSUB']"))
    )

    elements = driver.find_elements(By.XPATH, "//span[@ng-bind-html='cann.NEWSSUB']")



    # Extracting the names of companies and avoiding duplicates
    for element in elements:
        element = element.text
        name = element.split('-')[0].strip()
        
        if name in company:
            pass
        else:
            company.append(name)
    print(company)
    driver.quit()
    return company

scrapper()   