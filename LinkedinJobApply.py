from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
import time

def select_country():
    try:
        # Try to find the dropdown and select the country code if present
        dropdown = driver.find_element(By.XPATH, "//*[contains(@id, '-phoneNumber-country')]")
        select = Select(dropdown)
        for option in select.options:
            if "+91" in option.get_attribute("value"):
                select.select_by_value(option.get_attribute("value"))
                break
    except:
        pass

def click_job_apply():
    try:
        apply_button = driver.find_element(By.XPATH, "//button[contains(@class, 'jobs-apply-button')]")        
        apply_button.click()    
        time.sleep(4)        
    except:
        # If phone input is also not found, move to next button click loop
        pass

def enter_phone():
    try:
        phone_input = driver.find_element(By.XPATH, "//*[contains(@id, '-phoneNumber-nationalNumber')]")
        if not phone_input.get_attribute("value").strip():
            phone_input.send_keys("7698784947") 
    except:
        # If phone input is also not found, move to next button click loop
        pass

def click_next_until_found():
    submit_click = False
    j = 0
    while (submit_click == False):
        try:
            # Try to find the 'Next' button and click it
            next_button = driver.find_element(By.XPATH, '//button[@aria-label="Continue to next step"]')
            next_button.click()
            time.sleep(4)
            
        except:
            pass  # If the next button is not found, continue looping

        # Check if the 'Review' button is found
        try:
            review_button = driver.find_element(By.XPATH, '//button[@aria-label="Review your application"]')
            review_button.click()
            time.sleep(4)
            
        except:
            pass  # If the review button is not found, continue looping

        # Check if the 'Submit' button is found
        try:
            submit_button = driver.find_element(By.XPATH, '//button[@aria-label="Submit application"]')
            submit_button.click()
            submit_click = True
            time.sleep(4)
            
            dismiss_button = driver.find_element(By.XPATH, '//button[@aria-label="Dismiss"]')
            dismiss_button.click()            
            time.sleep(4)

        except:
            pass  # If the submit button is not found, continue looping
        
        j = j + 1
        try:
            if(j == 10):
                dismiss_button = driver.find_element(By.XPATH, '//button[@aria-label="Dismiss"]')
                dismiss_button.click()
                time.sleep(4)

                discard_button = driver.find_element(By.XPATH, '//button[@data-control-name="discard_application_confirm_btn"]')
                discard_button.click()
                time.sleep(4)
                break
        except:
            if(j == 10):
                break
            pass       
# Setup WebDriver
# Download chrome by using following url with your chrome version 
# https://googlechromelabs.github.io/chrome-for-testing/
s = Service(r'chromedriver-win64\chromedriver.exe')
driver = webdriver.Chrome(service=s)
driver.get("https://www.linkedin.com/login?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin")
time.sleep(5)

# Manual login required
username_input = driver.find_element(By.ID, value="username")
username_input.send_keys("*******") # set the actual email here

password_input = driver.find_element(By.ID, value="password")
password_input.send_keys("********") # set the actual password here

btnSignIn = driver.find_element(By.CSS_SELECTOR, 'button[class="btn__primary--large from__button--floating"]')
btnSignIn.click()
time.sleep(4)

i = 0
if(i == 0):
    driver.get("https://www.linkedin.com/jobs/search/?currentJobId=4062716573&f_AL=true&f_E=4&f_TPR=r86400&f_WT=2&geoId=92000000&keywords=c%23&location=Worldwide&origin=JOB_SEARCH_PAGE_JOB_FILTER&refresh=true&sortBy=R")
else:
    i = i + 1
    count = i * 25
    driver.get(f"https://www.linkedin.com/jobs/search/?currentJobId=4062716573&f_AL=true&f_E=4&f_TPR=r86400&f_WT=2&geoId=92000000&keywords=c%23&location=Worldwide&origin=JOB_SEARCH_PAGE_JOB_FILTER&refresh=true&sortBy=R&start={count}")

time.sleep(4)  # wait for page to load
element_found = True
while(element_found == True):
    element_found == False
    elements = driver.find_elements(By.XPATH, "//a[contains(@class, 'job-card-container__link')]")    
    for element in elements:
        element_found = True        
        strong_text = element.find_element(By.XPATH, ".//strong").text.lower()            
        if not any(keyword in strong_text for keyword in ["c#", ".net", "dotnet", "dot net"]):
            continue
        
        element.click()
        time.sleep(4)

        click_job_apply()
        select_country()
        enter_phone()        
        click_next_until_found()
        time.sleep(5)
        

    i = i + 1
    count = i * 25
    driver.get(f"https://www.linkedin.com/jobs/search/?currentJobId=4062716573&f_AL=true&f_E=4&f_TPR=r86400&f_WT=2&geoId=92000000&keywords=c%23&location=Worldwide&origin=JOB_SEARCH_PAGE_JOB_FILTER&refresh=true&sortBy=R&start={count}")
    time.sleep(5)  # wait for page to load
    print(f"Set i for {i} while next run")
