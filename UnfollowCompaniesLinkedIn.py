from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager

import time

# Setup WebDriver
s = Service('C:\Rakesh\DummyProject\TailorManagementGithub\chromedriver-win64\chromedriver.exe')
driver = webdriver.Chrome(service=s)
driver.get("https://www.linkedin.com")
time.sleep(2)

# driver.get("https://www.linkedin.com/in/rakeshkumar-gohil-812897194/details/interests/?detailScreenTabIndex=0")

# Manual login required
username_input = driver.find_element(By.ID, value="session_key")
username_input.send_keys("youremail") # set the actual email here

password_input = driver.find_element(By.ID, value="session_password")
password_input.send_keys("yourpassword") # set the actual password here

btnSignIn = driver.find_element(By.CSS_SELECTOR, 'button[data-id="sign-in-form__submit-btn"]')
btnSignIn.click()
time.sleep(5)


try:
    # #=============================Uncomment this section for company unfollowing=============================
    # driver.get("https://www.linkedin.com/in/rakeshkumar-gohil-812897194/details/interests/?detailScreenTabIndex=0")
    # time.sleep(5)  # wait for page to load

    # # Loop to unfollow companies
    # while True:
    #     elements = driver.find_elements(By.XPATH, "//span[@class='artdeco-button__text' and text()='Following']")
    #     for element in elements:
    #         element.click()

    #=============================Uncomment this section for page unfollowing=================================
    
    driver.get("https://www.linkedin.com/mynetwork/network-manager/company")
    time.sleep(5)  # wait for page to load

    # Loop to unfollow companies
    
    elements = driver.find_elements(By.XPATH, "//span[@class='artdeco-button__text' and text()='Following']")
    for element in elements:
        element.click()
        time.sleep(1)
        unfollowbutton = driver.find_element(By.XPATH, "//span[@class='artdeco-button__text' and text()='Unfollow']")
        
        unfollowbutton.click()
        time.sleep(1)

finally:
    driver.quit()

