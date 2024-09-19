# Automation of simple user actions (hiding fields, hovering the mouse over a web element, extracting data from a web table and iframe, handling browser alert)
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

URL = "replaceme"

# To keep the browser window opened
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

# Create and configure driver
driver = webdriver.Chrome(options=chrome_options)
driver.get(URL)

#Search for a product and check if matching products are found
search_key = "berry" # will find several results, that contain this search key
driver.find_element(By.CLASS_NAME, "search-keyword").send_keys(search_key)
driver.find_element(By.CLASS_NAME, "search-button").click()
time.sleep(2)
results = driver.find_elements(By.TAG_NAME, "h4")
count = len(results)
assert count == 2
for item in results:
    assert search_key in item.text

# End program execution
driver.quit()
