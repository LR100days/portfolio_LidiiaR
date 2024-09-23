from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

URL = "replace"

# To keep the browser window opened
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

# Create and configure driver
driver = webdriver.Chrome(options=chrome_options)
driver.implicitly_wait(3)
driver.maximize_window()
driver.get(URL)

# Switch to Iframe
driver.switch_to.frame("courses-iframe")

#Set mouse-driver interaction
action = ActionChains(driver)

#Hover on text and verify options
action.move_to_element(driver.find_element(By.CLASS_NAME, "dropdown-toggle")).perform()
expected_list = ["About Us", "Contact"]
for option in expected_list:
    actual_option = driver.find_element(By.LINK_TEXT, f"{option}")
    assert actual_option.text == option

# End program execution
driver.quit()


