from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC, expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

URL = "replaceme"
PASSWORD = "replaceme"

# To keep the browser window opened
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

# Create and configure driver
driver = webdriver.Chrome(options=chrome_options)
driver.get(URL)

# Follow link and retrieve the email address for invalid username from another tab
link = driver.find_element(By.CLASS_NAME, "blinkingText").click()

windowsOpened = driver.window_handles
driver.switch_to.window(windowsOpened[1])

username = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="interview-material-container"]/div/div[2]/p[2]/strong/a')))
invalid_username = username.text

driver.close()
driver.switch_to.window(windowsOpened[0])

# Find the input fields
username_field = driver.find_element(By.ID, "username").send_keys(invalid_username, Keys.TAB)
password_field = driver.find_element(By.ID, "password").send_keys(PASSWORD, Keys.TAB)
terms_checkbox = driver.find_element(By.ID, "terms").click()
submit = driver.find_element(By.ID, "signInBtn")

# Verify an error message,print the message to console
alert_window = WebDriverWait(driver, 4).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.alert-danger')))
alert_text = driver.execute_script("return document.querySelector('.alert-danger').textContent.trim();")

assert "Incorrect" in alert_text

# End program execution
driver.quit()

# driver.close() - to close certain tab
# driver.quit() - to end the program execution completely