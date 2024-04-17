from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time

def find_element_safe(driver, by, value):
    try:
        return driver.find_element(by, value)
    except:
        return None

# Setup WebDriver
s = Service('C:\Rakesh\DummyProject\TailorManagementGithub\chromedriver-win64\chromedriver.exe')
driver = webdriver.Chrome(service=s)
driver.get("https://www.seek.com.au/oauth/login/?returnUrl=https%3A%2F%2Fwww.seek.com.au%2F")
time.sleep(10)

# Manual login required
username_input = driver.find_element(By.ID, value="emailAddress")
username_input.send_keys("youremail") # set the actual email here

password_input = driver.find_element(By.ID, value="password")
password_input.send_keys("yourpassword") # set the actual password here

btnSingIn = driver.find_element(By.XPATH, "//button[@class='lv79p50 lv79p57 u6fs7f62 u6fs7fp u6fs7f5e u6fs7f4y u6fs7fy u6fs7fx u6fs7f5 u6fs7fh6 u6fs7f4 u6fs7fh y1i63n0 y1i63n6 _1qrvu3719 _1qrvu371b u6fs7f16 u6fs7f17']")
btnSingIn.click()
time.sleep(10)

hrefsAll = []
hrefsSubmitted = []
hrefsNotSubmitted = []

try:
    i = 1
    isJobOver1day = False
    while(isJobOver1day == False):
        driver.get("https://www.seek.com.au/c%23-jobs?daterange=3&sortmode=ListedDate&page="+str(i))
        time.sleep(15)

        job_titles = driver.find_elements(By.CSS_SELECTOR, 'a[data-automation="jobTitle"]')
        for job_title in job_titles:
            if 'c#' in job_title.text.lower() or '.net' in job_title.text.lower():
                href = job_title.get_attribute('href')
                hrefsAll.append(href)

        job_listing_dates = driver.find_elements(By.CSS_SELECTOR, 'span[data-automation="jobListingDate"]')
        for job_listing_date in job_listing_dates:
            if '1d ago' in job_listing_date.text.lower():
                isJobOver1day = True
                break

        i = i + 1

    for href in hrefsAll:
        print(href)
        driver.get(href)
        btnQuickApply = driver.find_element(By.CSS_SELECTOR, 'a[data-automation="job-detail-apply"]')
        if(btnQuickApply.text.lower() != 'quick apply'):
            hrefsNotSubmitted.append(href)
            print("not submitted")
            continue
        if(btnQuickApply is not None):
            btnQuickApply.click()
            time.sleep(3)
            btnContinueFound = True
            i = 1
            while(btnContinueFound == True and i < 10):
                btnContinue = find_element_safe(driver, By.CSS_SELECTOR, 'button[data-testid="continue-button"]')
                
                if(btnContinue is None):
                    btnContinueFound = False
                else:
                    btnContinue.click()
                    time.sleep(3)
                i = i + 1
            
            btnSubmit = find_element_safe(driver, By.CSS_SELECTOR, 'button[data-testid="review-submit-application"]')
            if(btnSubmit is not None):
                btnSubmit.click()
                time.sleep(3)         
                print("submitted")       
                hrefsSubmitted.append(href)
            else:
                print("not submitted")
                hrefsNotSubmitted.append(href)

    for href in hrefsNotSubmitted:
        print("not submitted hrefssssssssss")
        print(href)
        js_script = f"window.open('{href}', '_blank');"
        driver.execute_script(js_script)
    
    input("Press any key to exit but before exit complete the applications")
finally:
    driver.quit()


