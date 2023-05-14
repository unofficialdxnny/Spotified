from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from time import sleep


# open username and password files
with open('username.txt', 'r') as f:
    usernames = f.read().splitlines()
with open('password.txt', 'r') as f:
    passwords = f.read().splitlines()

# initialize a Chrome browser instance
options = Options()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options)

# navigate to Spotify's login page
driver.get('https://www.spotify.com/login/')

# loop through the usernames and passwords and attempt to log in with each one
for i in range(len(usernames)):
    # enter the username and password

    username = driver.find_element(By.ID, 'login-username')

    password = driver.find_element(By.ID, 'login-password')
    username.clear()
    password.clear()
    username.send_keys(usernames[i])
    password.send_keys(passwords[i])

    # click the login button
    login_button = driver.find_element(By.ID, 'login-button')
    login_button.click()



sleep(5)
driver.get('https://open.spotify.com/user/ahmeddanial')


sleep(7)
# click the follow button
follow_button = driver.find_element(By.XPATH, '/html/body/div[4]/div/div[2]/div[4]/div[1]/div[2]/div[2]/div/div/div[2]/main/section/div/div[3]/div[4]/div/div/div/div/button[1]')

if follow_button.text == 'FOLLOW':
    follow_button.click()
    print("Followed user ahmeddanial")
else:
    print("Already following user ahmeddanial")

# close the browser window
driver.quit()
