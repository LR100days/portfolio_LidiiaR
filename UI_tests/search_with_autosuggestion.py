# This test verifies that list of autosuggestion, based on user search, is displayed, and user can select desired option from the list.

import random
from selenium import webdriver
from selenium.webdriver.common.by import By

URL = "rename"

# To keep the browser window opened
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

# Create and configure driver
driver = webdriver.Chrome(options=chrome_options)
driver.implicitly_wait(3)
driver.get(URL)

# Find the search field and input a part of search text
test_data = ["Germany", "Argentina", "United Arab Emirates", "Hungary", "Denmark"]
search_text = random.choice(test_data)

driver.find_element(By.ID, "autosuggest").send_keys(search_text[:2])
countries_list = driver.find_elements(By.CLASS_NAME, "ui-menu-item a")
for country in countries_list:
    if country.text == search_text:
        country.click()
        break

# Verify that selected search item from list of autosuggestions is displayed in the Search field
current_country = driver.find_element(By.ID, "autosuggest").get_attribute("value")
assert current_country == search_text

# End program execution
driver.quit()
