
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

URL = "replace"

# To keep the browser window opened
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

# Create and configure driver
driver = webdriver.Chrome(options=chrome_options)
driver.implicitly_wait(5)
driver.get(URL)
# Go to the shopping page
driver.find_element(By.CSS_SELECTOR, "a[href*='shop']").click()

#Search for product and add to the cart
list = driver.find_elements(By.XPATH, "//div[@class='card h-100']")
for product in list:
    productName = product.find_element(By.XPATH, "div/h4/a").text
    if productName == "Blackberry":
        product.find_element(By.XPATH, "div/button").click()

checkout = driver.find_element(By.XPATH, "//a[@class='nav-link btn btn-primary']").click()

# Verify added product
added_product = driver.find_element(By.TAG_NAME, "h4")
total_sum = driver.find_element(By.XPATH, "//h3/strong")
assert added_product.text == "Blackberry"
assert total_sum.text == "₹. 50000"

# Proceed to checkout
driver.find_element(By.XPATH,"//button[@class='btn btn-success']").click()
driver.find_element(By.ID,"country").send_keys("Ukr")
wait = WebDriverWait(driver,10)
wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT,"Ukraine")))

driver.find_element(By.LINK_TEXT,"Ukraine").click()
driver.find_element(By.XPATH,"//div[@class='checkbox checkbox-primary']").click()
driver.find_element(By.CSS_SELECTOR,"[type='submit']").click()

# Verify that order is successfully completed
success_message = driver.find_element(By.CLASS_NAME,"alert-success").text
assert "Success! Thank you!" in success_message

# End program execution
driver.quit()

