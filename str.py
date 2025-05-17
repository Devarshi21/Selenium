import streamlit as st
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
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//span[@ng-bind-html='cann.NEWSSUB']"))
    )
    elements = driver.find_elements(By.XPATH, "//span[@ng-bind-html='cann.NEWSSUB']")
    for element in elements:
        element = element.text
        name = element.split('-')[0].strip()
        
        if name in company:
            pass
        else:
            company.append(name)
    driver.quit()
    return company

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
            element.send_keys(Keys.ENTER)
            break

    market_value = driver.find_element(By.CLASS_NAME, "number").text
    company_value = (market_value + "Cr")  # Printing the market cap of the company
    print(f"Market Cap of {company_name} is: {company_value}")
    driver.quit()
    return company_value

try:
    st.write("List of companies with order updates:")
    if st.button("Get Company List"):
        with st.spinner("Scraping data..."):
            company_list = scrapper()
            st.write(company_list)
            cap = screener(company_list[0].split(' ')[0] + " " + company_list[0].split(' ')[1])
            st.write(f"Market Cap of {company_list[0]} is: {cap}")
except Exception as e:
    st.write("Cannot fetch data")

