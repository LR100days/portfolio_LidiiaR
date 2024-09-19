import time

from selenium import webdriver
from selenium.webdriver.common.by import By

URL = "replace"

# To keep the browser window opened
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

# Create and configure driver
driver = webdriver.Chrome(options=chrome_options)
driver.get(URL)

#Search for a products
search_key = "berry" # will find 2 results, that contain this search key
driver.find_element(By.CLASS_NAME, "search-keyword").send_keys(search_key)
driver.find_element(By.CLASS_NAME, "search-button").click()
time.sleep(2)
results = driver.find_elements(By.TAG_NAME, "h4")
for item in results:
    assert search_key in item.text

# Add the products to the cart
products = driver.find_elements(By.XPATH, "//div[@class='products']/div")
for item in products:
    item.find_element(By.XPATH, "div/button").click()

added_items = driver.find_element(By.XPATH, "//div[@class='cart-info']/table/tbody/tr[1]/td[3]/strong")
assert added_items.text == "2"

# End program execution
driver.quit()
