import time
import random

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

URL = "replaceme"
USERNAME = "replaceme"
PASSWORD = "replaceme"

# To keep the browser window opened
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

# Create and configure driver
driver = webdriver.Chrome(options=chrome_options)
driver.get(URL)

# Find the input fields and insert valid data
username_field = driver.find_element(By.ID, "username").send_keys(USERNAME)
password_field = driver.find_element(By.ID, "password").send_keys(PASSWORD)

# Change radiobutton and verify that confirmation message is present
radio_buttons = driver.find_elements(By.CSS_SELECTOR, ".checkmark")
radio_buttons[1].click()
time.sleep(1)
modal_text = driver.find_element(By.CSS_SELECTOR, ".modal-body p")
assert "Proceed?" in modal_text.text
accept = driver.find_element(By.CSS_SELECTOR, "#okayBtn").click()

# Select another option in dropdown
dropdown = driver.find_elements(By.XPATH, "//*[@id='login-form']/div[5]/select/option")
options_list = []

# Random selection of available options in the dropdown, skip the default option
for option in dropdown:
    # Get the value and text for each option
    new_key = option.get_attribute("value")
    new_option = option.text
    if new_option == "Student":
        pass
    else:
        # Append a tuple (new_key, new_option) to the list
        options_list.append((new_key, new_option))

random_option_pair = random.choice(options_list)
random_option_key = random_option_pair[0]
random_option_value = random_option_pair[1]

open_dropdown = driver.find_element(By.CSS_SELECTOR, ".form-control").click()
select_option = driver.find_element(By.XPATH, f"//*[@id='login-form']/div[5]/select/option[@value='{random_option_key}']").click()

# Verify selected option in the dropdown
get_selected_value = Select(driver.find_element(By.XPATH, "//*[@id='login-form']/div[5]/select"))
current_option = get_selected_value.first_selected_option.text
assert random_option_value == current_option

# Accept terms and conditions and submit
terms_checkbox = driver.find_element(By.ID, "terms").click()
submit = driver.find_element(By.ID, "signInBtn").click()

# Verify that user is logged in
home_page = WebDriverWait(driver, 7).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".navbar-brand")))
assert "ProtoCommerce" in home_page.text

# End program execution
driver.quit()
