from selenium import webdriver
from selenium.webdriver.common.by import By

URL = "replaceme"

# To keep the browser window opened
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

# Create and configure driver
driver = webdriver.Chrome(options=chrome_options)
driver.implicitly_wait(3)
driver.get(URL)

# Handling Java pop-up
user_input = driver.find_element(By.ID, "name").send_keys("My name")
driver.find_element(By.ID, "alertbtn").click()
alert = driver.switch_to.alert
assert "My name" in alert.text
alert.accept()
# alert.dismiss()

# End program execution
driver.quit()
