from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time, os
from read import read_the_file
from dotenv import load_dotenv
load_dotenv()

email_id = os.getenv("EMAIL")
password = os.getenv("PASS")
file_path = "/home/dedsec995/Documents/Parking/10-10.ods"
selected_sheet = "12-2"
df = read_the_file(file_path, selected_sheet)
desired_option = {
    "8-10": "8  -  9:59 AM",
    "10-12": "10  -  11:59 AM",
    "12-2": "12  -  1:59  PM",
}

desired_option_text = desired_option[selected_sheet]
selected_loop = "Central Loop (Blue)"


# Function to fill out the form
def fill_form(row_data):

    # Check and click the checkbox
    checkbox = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (
                By.XPATH,
                "//div[@role='checkbox' and @aria-label='Record aluhar1@binghamton.edu as the email to be included with my response']",
            )
        )
    )
    if not checkbox.get_attribute("aria-checked") == "true":
        checkbox.click()
        time.sleep(1)

    # Click Next
    next_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            (By.XPATH, "//span[@class='NPEfkd RveJvd snByac' and text()='Next']")
        )
    )
    next_button.click()
    time.sleep(1)
    # Select time slot
    select_option(desired_option_text, "div[role='listbox']")

    # Click Next
    next_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            (By.XPATH, "//span[@class='NPEfkd RveJvd snByac' and text()='Next']")
        )
    )
    next_button.click()
    time.sleep(1)
    # Select loop
    select_option(selected_loop, "div[role='listbox']")

    # Click Next
    next_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            (By.XPATH, "//span[@class='NPEfkd RveJvd snByac' and text()='Next']")
        )
    )
    next_button.click()
    time.sleep(1)
    # Select row
    select_option(row_data[0], "div[role='listbox']")

    # Click Next
    next_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            (By.XPATH, "//span[@class='NPEfkd RveJvd snByac' and text()='Next']")
        )
    )
    next_button.click()
    time.sleep(1)
    # Input data from the next column (row[1])
    input_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "input.whsOnd.zHQkBf"))
    )
    input_field.clear()
    input_field.send_keys(str(row_data[1]))
    time.sleep(1)
    # Click Next
    next_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            (By.XPATH, "//span[@class='NPEfkd RveJvd snByac' and text()='Next']")
        )
    )
    next_button.click()

    time.sleep(1)
    # First input field (row[2])
    input_field1 = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "input[aria-labelledby='i1']"))
    )
    input_field1.clear()
    input_field1.send_keys(str(row_data[2]))

    # Second input field (row[3])
    input_field2 = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "input[aria-labelledby='i5']"))
    )
    input_field2.clear()
    input_field2.send_keys(str(row_data[3]))

    # Third input field (row[4])
    input_field3 = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "input[aria-labelledby='i9']"))
    )
    input_field3.clear()
    input_field3.send_keys(str(row_data[4]))

    # Fourth input field (row[5])
    input_field4 = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "input[aria-labelledby='i13']"))
    )
    input_field4.clear()
    input_field4.send_keys(str(row_data[5]))

    # Fifth input field (row[6])
    input_field5 = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "input[aria-labelledby='i17']"))
    )
    input_field5.clear()
    input_field5.send_keys(str(row_data[6]))

    # Sixth input field (row[7])
    input_field6 = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "input[aria-labelledby='i21']"))
    )
    input_field6.clear()
    input_field6.send_keys(str(row_data[7]))

    # Seventh input field (row[8])
    input_field7 = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "input[aria-labelledby='i25']"))
    )
    input_field7.clear()
    input_field7.send_keys(str(row_data[8]))

    # Eighth input field (row[9])
    input_field8 = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "input[aria-labelledby='i29']"))
    )
    input_field8.clear()
    input_field8.send_keys(str(row_data[9]))
    
    # Click Next
    next_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            (By.XPATH, "//span[@class='NPEfkd RveJvd snByac' and text()='Next']")
        )
    )
    next_button.click()
    time.sleep(1)
    
    next_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            (By.XPATH, "//span[@class='NPEfkd RveJvd snByac' and text()='Next']")
        )
    )
    next_button.click()
    time.sleep(1)
    
    submit_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            (By.XPATH, "//span[@class='NPEfkd RveJvd snByac' and text()='Submit']")
        )
    )
    submit_button.click()


def select_option(desired_option_text, dropdown_selector):
    dropdown = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, dropdown_selector))
    )
    time.sleep(1)
    selected_option = dropdown.find_element(
        By.CSS_SELECTOR, "div[aria-selected='true']"
    )
    current_selection = (
        selected_option.get_attribute("data-value") if selected_option else None
    )

    if current_selection != desired_option_text:
        dropdown.click()
        time.sleep(1)

        desired_option = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(
                (
                    By.XPATH,
                    f"//div[@role='option' and @data-value='{desired_option_text}']",
                )
            )
        )
        desired_option.click()
        time.sleep(1)


driver = webdriver.Chrome()

# Login process (only needed once)
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
time.sleep(2)

get2fa = input("2FA Done?: ")

# Iterate through each row in the dataframe
for index, row in df.iterrows():
    print(f"Starting {row[0]}")
    driver.execute_script("window.open('');")
    driver.switch_to.window(driver.window_handles[-1])
    driver.get(
        "https://docs.google.com/forms/d/e/1FAIpQLSe_UTDrBFTTVCXR8B4V_YB76g2wb5ulvUpCbKRnkJKNDImOBQ/viewform"
    )
    fill_form(row)
    print(f"Done {row[0]}")
    time.sleep(2)  # Wait between submissions

print("Done with all the Parking lots.")
print("Closing in 90 seconds.")
time.sleep(90)
driver.quit()
