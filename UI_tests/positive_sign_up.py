from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

URL = "replaceme"
VALID_NAME = "MyFirstName"
VALID_LAST_NAME= "MyLastName"
EMAIL = "replaceme"

# To keep the browser window opened
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

# Create and configure driver
# chrome_options.add_argument("headless") # to run without UI
# chrome_options.add_argument("--ignore-certificate-errors") # ignores SSL certificate errors
driver = webdriver.Chrome(options=chrome_options)
driver.get(URL)

# Find the input fields and enter data
name = driver.find_element(By.NAME, value="fName").send_keys(VALID_NAME, Keys.TAB)
last_name = driver.find_element(By.NAME, value="lName").send_keys(VALID_LAST_NAME, Keys.TAB)
email = driver.find_element(By.NAME, value="email").send_keys(EMAIL)

# Submit entered data
submit_button = driver.find_element(By.CLASS_NAME, value="btn-block").click()

# Verify that user is signed in
success_message = driver.find_element(By.CLASS_NAME, value="lead")
assert "successfully subscribed" in success_message.text

# End program execution
driver.quit()