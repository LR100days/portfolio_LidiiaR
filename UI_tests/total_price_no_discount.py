import time
from selenium import webdriver
from selenium.webdriver.common.by import By

URL = "replace"

# To keep the browser window opened
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

# Create and configure driver
driver = webdriver.Chrome(options=chrome_options)
driver.implicitly_wait(2)
driver.get(URL)

#Search for products and add to the cart
search_key = "berry" # will find 2 results, that contain this search key
driver.find_element(By.CLASS_NAME, "search-keyword").send_keys(search_key)
driver.find_element(By.CLASS_NAME, "search-button").click()
time.sleep(1)
products = driver.find_elements(By.XPATH, "//div[@class='products']/div")
# Add to cart
for item in products:
    item.find_element(By.XPATH, "div/button").click()

cart = driver.find_element(By.CSS_SELECTOR, "img[alt='Cart']").click()
proceed_to_checkout = driver.find_element(By.XPATH, "//button[text()='PROCEED TO CHECKOUT']").click()

# Validate total sum
prices = driver.find_elements(By.XPATH, "//td[5]/p")
expected_sum = 0
for price in prices:
    expected_sum += int(price.text)

actual_total_sum = driver.find_element(By.CSS_SELECTOR, ".totAmt")
assert expected_sum == int(actual_total_sum.text)

# Validate default discount
discount = driver.find_element(By.CSS_SELECTOR, ".discountPerc")
assert discount.text == "0%"

# Validate total sum to pay
sum_after_discount = driver.find_element(By.CSS_SELECTOR, ".discountAmt")
assert expected_sum == int(sum_after_discount.text)

# End program execution
driver.quit()
