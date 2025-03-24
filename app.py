from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Define the values to enter
plate_number = "plate"
time_required = "2 hours"
discount_code = "code"
email_address = "email"

# Set up the WebDriver
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")  # Open browser in full screen
driver = webdriver.Chrome(options=options)

try:
    # Open the webpage
    url = "https://hotspotparking.com/tapPoster/park/CarletonTemp111"
    driver.get(url)

    # Wait for the input fields to be visible
    wait = WebDriverWait(driver, 10)

    # Find and populate the Plate Number field
    plate_input = wait.until(EC.presence_of_element_located((By.ID, "plate")))
    plate_input.send_keys(plate_number)

    # Find and populate the Time field
    plate_input = wait.until(EC.presence_of_element_located((By.ID, "time")))
    plate_input.send_keys(time_required)

    # Find and populate the Discount Code field
    discount_input = wait.until(EC.presence_of_element_located((By.ID, "discount-code")))
    discount_input.send_keys(discount_code)

    # Wait for the Proceed button to be present
    proceed_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Park')]")))

    # Click the button
    proceed_button.click()

    # Wait to observe the result
    wait.until(EC.url_changes(url))

    # Wait for the input fields to be visible
    wait = WebDriverWait(driver, 10)

    # Find and populate the Email field
    plate_input = wait.until(EC.presence_of_element_located((By.ID, "email")))
    plate_input.send_keys(email_address)

    # Click outside the input field to remove focus
    body = driver.find_element(By.TAG_NAME, "body")
    body.click()

    # Wait for the Send button to be present
    proceed_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Send')]")))

    # Click the button
    proceed_button.click()

    # Wait to observe the result
    wait.until(EC.url_changes(url))

finally:
    # Close the browser
    # driver.quit()
    body = driver.find_element(By.TAG_NAME, "body")
    body.click()