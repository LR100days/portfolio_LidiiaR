from selenium import webdriver
from selenium.webdriver.common.by import By

URL = "replaceme"

# To keep the browser window opened
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

# Create and configure driver
driver = webdriver.Chrome(options=chrome_options)
driver.get(URL)

# Verify that textbox is not displayed after clicking on the Hide button
textbox = driver.find_element(By.ID, "displayed-text")
assert textbox.is_displayed()
driver.find_element(By.ID, "hide-textbox").click()
assert not textbox.is_displayed()

# End program execution
driver.quit()
