from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://www.google.com")


from selenium import webdriver
from selenium.webdriver.chrome.service import Service

s = Service('C:\Rakesh\DummyProject\TailorManagementGithub\chromedriver-win64\chromedriver.exe')
driver = webdriver.Chrome(service=s)


# Navigate to a website
driver.get("https://www.example.com")


# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager

# # Set the path to your user data and profile directory
# user_data_path = r"C:\Users\YourUserName\AppData\Local\Google\Chrome\User Data"  # Adjust path as necessary
# profile_name = "Profile 1"  # Adjust profile name as necessary

# # Create an instance of ChromeOptions
# options = Options()
# options.add_argument(f"user-data-dir={user_data_path}")
# options.add_argument(f"profile-directory={profile_name}")

# # Initialize WebDriver with these options
# service = Service(ChromeDriverManager().install())
# driver = webdriver.Chrome(service=service, options=options)

# # Open a webpage
# driver.get("https://www.example.com")

from webdriver_manager.chrome import ChromeDriverManager
print("webdriver-manager is successfully imported!")

# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager

# # Set the path to your user data and profile directory
# user_data_path = r"C:\Users\YourUserName\AppData\Local\Google\Chrome\User Data"  # Adjust path as necessary
# profile_name = "Profile 1"  # Adjust profile name as necessary

# # Create an instance of ChromeOptions
# options = Options()
# options.add_argument(f"user-data-dir={user_data_path}")
# options.add_argument(f"profile-directory={profile_name}")

# # Initialize WebDriver with these options
# service = Service(ChromeDriverManager().install())
# driver = webdriver.Chrome(service=service, options=options)

# # Open a webpage
# driver.get("https://www.example.com")

from webdriver_manager.chrome import ChromeDriverManager
print("webdriver-manager is successfully imported!")
