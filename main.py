import time
import random
import string
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from time import sleep
import json
from datetime import datetime, timedelta


# Function to generate a random DOB
def generate_random_dob():
    today = datetime.today()
    min_age = 13
    max_year = today.year - min_age
    year = random.randint(1901, max_year)
    month = random.randint(1, 12)
    max_day = (
        (datetime(year, month + 1, 1) - timedelta(days=1)).day if month != 12 else 31
    )
    day = random.randint(1, max_day)
    return day, month, year


# Load JSON data
with open("./data/firstnames.json") as f:
    firstnames = json.load(f)

with open("./data/lastnames.json") as f:
    lastnames = json.load(f)

# Set up Chrome options
options = Options()
options.add_experimental_option("detach", True)

while True:
    # Initialize the Chrome driver with options
    driver = webdriver.Chrome(options=options)

    # Select random first and last names
    random_firstname = random.choice(firstnames)
    random_lastname = random.choice(lastnames)
    display_name = f"{random_firstname} {random_lastname}"

    # URL of the form to be filled
    url = "https://www.spotify.com/uk/signup?forward_url=https%3A%2F%2Fopen.spotify.com%2F"
    driver.get(url)

    sleep(2.5)

    # Check for the visibility of the button specified by the given XPath
    try:
        cookies_button = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(
                (
                    By.XPATH,
                    "/html/body/div[3]/div[2]/div/div[1]/div/div[2]/div/button[1]",
                )
            )
        )
        cookies_button.click()
        print("Clicked the visible button.")
    except Exception as e:
        print("The specified button was not visible or could not be clicked:", e)

    sleep(0.5)

    # Wait for the email field to be available
    email = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "username"))
    )

    # Fill the form with random details
    characters = string.ascii_letters + string.digits
    random_email = "".join(random.choice(characters) for _ in range(25)) + "@gmail.com"
    email.send_keys(random_email)

    sleep(0.5)
    next_button = driver.find_element(
        By.XPATH, "/html/body/div[1]/main/main/section/div/form/button/span[1]"
    )
    next_button.click()

    sleep(0.5)
    password = "spot_ified"
    password_field = driver.find_element(
        By.XPATH,
        "/html/body/div[1]/main/main/section/div/form/div[1]/div[2]/div/section/div[2]/div/div[2]/div[1]/input",
    )
    password_field.send_keys(password)

    sleep(0.5)
    next_button = driver.find_element(
        By.XPATH, "/html/body/div[1]/main/main/section/div/form/div[2]/button/span[1]"
    )
    next_button.click()

    sleep(0.5)

    # Wait for the display name input to be available and send the combined name
    try:
        display_name_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    "/html/body/div[1]/main/main/section/div/form/div[1]/div[2]/div/section/div[3]/div[1]/div[2]/input",
                )
            )
        )
        display_name_input.send_keys(display_name)
        print(f"Sent display name: {display_name}")
    except Exception as e:
        print("The display name input was not found:", e)

    sleep(0.5)

    # Generate and store the DOB in variables
    day, month, year = generate_random_dob()
    d_input = driver.find_element(
        By.XPATH,
        "/html/body/div[1]/main/main/section/div/form/div[1]/div[2]/div/section/div[3]/div[2]/div[2]/div/input[1]",
    )
    d_input.send_keys(day)

    sleep(0.5)

    # Select the month
    month_input = driver.find_element(
        By.XPATH,
        "/html/body/div[1]/main/main/section/div/form/div[1]/div[2]/div/section/div[3]/div[2]/div[2]/div/div/select",
    )
    month_names = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December",
    ]
    first_letter = month_names[month - 1][0].upper()
    month_input.send_keys(first_letter)

    sleep(0.5)

    # Continue with the year
    year_input = driver.find_element(
        By.XPATH,
        "/html/body/div[1]/main/main/section/div/form/div[1]/div[2]/div/section/div[3]/div[2]/div[2]/div/input[2]",
    )
    year_input.send_keys(year)

    sleep(0.5)

    # List of genders
    gender_options = ["male", "female", "non-binary", "Something Else", "pnts"]

    # Randomly select a gender
    selected_gender = random.choice(gender_options)
    print(f"Selected gender: {selected_gender}")

    # Define the XPaths for each gender option
    gender_xpaths = {
        "male": "/html/body/div[1]/main/main/section/div/form/div[1]/div[2]/div/section/div[3]/fieldset/div/div/div[1]/label/span[1]",
        "female": "/html/body/div[1]/main/main/section/div/form/div[1]/div[2]/div/section/div[3]/fieldset/div/div/div[2]/label/span[1]",
        "non-binary": "/html/body/div[1]/main/main/section/div/form/div[1]/div[2]/div/section/div[3]/fieldset/div/div/div[3]/label/span[1]",
        "Something Else": "/html/body/div[1]/main/main/section/div/form/div[1]/div[2]/div/section/div[3]/fieldset/div/div/div[4]/label/span[1]",
        "pnts": "/html/body/div[1]/main/main/section/div/form/div[1]/div[2]/div/section/div[3]/fieldset/div/div/div[5]/label/span[1]",
    }

    # Locate and click the corresponding gender option based on the selected gender
    try:
        gender_input = driver.find_element(By.XPATH, gender_xpaths[selected_gender])
        gender_input.click()
        print(f"Clicked the gender option: {selected_gender}")
    except Exception as e:
        print(f"Error clicking the gender option: {e}")

    sleep(0.5)

    # Continue
    after_dob_form = driver.find_element(
        By.XPATH, "/html/body/div[1]/main/main/section/div/form/div[2]/button/span[1]"
    )
    after_dob_form.click()

    sleep(0.5)

    # Signup
    signup = driver.find_element(
        By.XPATH, "/html/body/div[1]/main/main/section/div/form/div[2]/button/span[1]"
    )
    signup.click()
    print("Form filled. Waiting for URL to change...")

    sleep(5)
    # Store account details in a text file
    text_filename = "./data/accounts/account_details.txt"
    account_details = f"{random_email}:{password}:{display_name}:{day}/{month}/{year}:{selected_gender}\n"

    # Write the account details to the text file
    with open(text_filename, mode="a") as textfile:
        textfile.write(account_details)

    print("Account details saved to text file.")

    # Wait for the URL to change to open.spotify.com
    WebDriverWait(driver, 30).until(EC.url_contains("open.spotify.com"))
    sleep(5)

    # Navigate to the specified URL
    url = "https://open.spotify.com/playlist/3FxsH4NU0U85AltRFy2i2n"  # replace this with your playlist or profile URL
    driver.get(url)

    sleep(2.5)

    # Check the URL and perform actions accordingly
    current_url = driver.current_url

    if "playlist" in current_url:
        # Click on the button for playlists
        try:
            playlist_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable(
                    (
                        By.XPATH,
                        "/html/body/div[5]/div/div[2]/div[4]/div[1]/div[2]/div[2]/div/main/section/div[2]/div[2]/div[2]/div/div/button[1]/span",
                    )
                )
            )
            playlist_button.click()
            print("Clicked the playlist button.")
        except Exception as e:
            print("Could not click the playlist button:", e)

    elif "user" in current_url:
        # Click on the button for user profiles
        try:
            user_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable(
                    (
                        By.XPATH,
                        "/html/body/div[5]/div/div[2]/div[4]/div[1]/div[2]/div[2]/div/main/section/div/div[3]/div[2]/div/div/button[1]",
                    )
                )
            )
            user_button.click()
            print("Clicked the user button.")
        except Exception as e:
            print("Could not click the user button:", e)

    else:
        print("What the heck is that URL you provided?")

    # Close the browser
    driver.quit()
    sleep(2)  # Optional: sleep before the next iteration
