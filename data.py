from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from read import read_the_file


email_id = "email_id"
password = "pass"
file_path = "8-19.ods"
selected_sheet = "12-2"
df = read_the_file(file_path, selected_sheet)
# print(df.head())

options = webdriver.ChromeOptions()
options.add_argument("user-data-dir=/home/dedsec995/.config/google-chrome/")
options.add_argument("--profile-directory=Default")

driver = webdriver.Chrome()

driver.get("https://www.google.com")
time.sleep(2) 

sign_in_button = driver.find_element(By.LINK_TEXT, "Sign in")
sign_in_button.click()
time.sleep(2)

email_input = driver.find_element(By.XPATH, "//input[@type='email']")
email_input.send_keys(email_id)
driver.find_element(By.XPATH, "//span[text()='Next']").click()
time.sleep(2)

password_input = driver.find_element(By.XPATH, "//input[@type='password']")
password_input.send_keys(password)
driver.find_element(By.XPATH, "//span[text()='Next']").click()
time.sleep(10)

get2fa = input("2FA Done?: ")

driver.get(
    "https://docs.google.com/forms/d/e/1FAIpQLSe_UTDrBFTTVCXR8B4V_YB76g2wb5ulvUpCbKRnkJKNDImOBQ/viewform"
)

checkbox = driver.find_element(
            By.XPATH,
            "//div[@role='checkbox' and @aria-label='Record aluhar1@binghamton.edu as the email to be included with my response']",
        )
if not checkbox.get_attribute("aria-checked") == "true":
    checkbox.click()
    time.sleep(1)

next_button_xpath = "//span[@class='NPEfkd RveJvd snByac' and text()='Next']"
next_button = driver.find_element(By.XPATH, next_button_xpath)
next_button.click()

options = {
    "1": "8  -  9:59 AM",
    "2": "10  -  11:59 AM",
    "3": "12  -  1:59  PM",
}

desired_option_text = options["1"]


# Wait for the dropdown to be present
dropdown = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, "div[role='listbox']"))
)

# Check if an option is already selected
selected_option = dropdown.find_element(By.CSS_SELECTOR, "div[aria-selected='true']")
current_selection = (
    selected_option.get_attribute("data-value") if selected_option else None
)

if current_selection != desired_option_text:
    # Click on the dropdown to open it
    dropdown.click()
    time.sleep(1)  # Wait for the dropdown to open

    # Find and click the desired option
    desired_option = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            (By.XPATH, f"//div[@role='option' and @data-value='{desired_option_text}']")
        )
    )
    desired_option.click()
    time.sleep(1)  # Wait for the selection to register

# Click the Next button
next_button_xpath = "//span[@class='NPEfkd RveJvd snByac' and text()='Next']"
next_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, next_button_xpath))
)
next_button.click()

# Wait for the dropdown to be present
selected_loop = "Central Loop (Blue)"
loop_dropdown = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, "div[role='listbox']"))
)

# Check if the correct option is already selected
selected_option = loop_dropdown.find_element(
    By.CSS_SELECTOR, "div[aria-selected='true']"
)
current_selection = (
    selected_option.get_attribute("data-value") if selected_option else None
)
print(current_selection)
if current_selection != selected_loop:
    # Click on the dropdown to open it
    loop_dropdown.click()
    time.sleep(1)  # Wait for the dropdown to open

    # Find and click the desired option
    desired_option = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            (By.XPATH, f"//div[@role='option' and @data-value='{selected_loop}']")
        )
    )
    desired_option.click()
    time.sleep(1)  # Wait for the selection to register

# Click the Next button
next_button_xpath = "//span[@class='NPEfkd RveJvd snByac' and text()='Next']"
next_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, next_button_xpath))
)
next_button.click()

selected_row = "D-(cap: 41)"

# Wait for the dropdown to be present
dropdown = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, "div[role='listbox']"))
)

# Check if an option is already selected
selected_option = dropdown.find_element(By.CSS_SELECTOR, "div[aria-selected='true']")
current_selection = (
    selected_option.get_attribute("data-value") if selected_option else None
)

if current_selection != selected_row:
    # Click on the dropdown to open it
    dropdown.click()
    time.sleep(1)  # Wait for the dropdown to open

    # Find and click the desired option
    desired_option = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            (By.XPATH, f"//div[@role='option' and @data-value='{selected_row}']")
        )
    )
    desired_option.click()
    time.sleep(1)  # Wait for the selection to register

# Click the Next button
next_button_xpath = "//span[@class='NPEfkd RveJvd snByac' and text()='Next']"
next_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, next_button_xpath))
)
next_button.click()

time.sleep(45000)
driver.quit()
