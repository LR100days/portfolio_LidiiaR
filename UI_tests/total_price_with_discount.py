import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

URL = "replace"
PROMO_CODE = "replace"

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

# Find total sum and expected discount
prices = driver.find_elements(By.XPATH, "//td[5]/p")
expected_sum = 0
for price in prices:
    expected_sum += float(price.text)

discount_value = 10 * expected_sum / 100
expected_sum_to_pay_with_discount = expected_sum - discount_value

# Apply discount
promo_code = driver.find_element(By.CSS_SELECTOR, ".promoCode").send_keys(PROMO_CODE)
apply_promo = driver.find_element(By.CSS_SELECTOR, ".promoBtn").click()
wait = WebDriverWait(driver,10)
wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR,".promoInfo")))

# Validate discount and sum to pay with applied discount
discount = driver.find_element(By.CSS_SELECTOR, ".discountPerc")
assert discount.text == "10%"
actual_sum_with_discount = driver.find_element(By.CSS_SELECTOR, ".discountAmt")
assert expected_sum_to_pay_with_discount == float(actual_sum_with_discount.text)

# End program execution
driver.quit()
