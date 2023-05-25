from pystyle import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from time import sleep
import os


os.system('cls')


banner = '''

⠀⠀⠀⠀⠀⠀⠀⢀⣠⣤⣤⣶⣶⣶⣶⣤⣤⣄⡀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢀⣤⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣤⡀⠀⠀⠀⠀
⠀⠀⠀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⠀⠀⠀
⠀⢀⣾⣿⡿⠿⠛⠛⠛⠉⠉⠉⠉⠛⠛⠛⠿⠿⣿⣿⣿⣿⣿⣷⡀⠀
⠀⣾⣿⣿⣇⠀⣀⣀⣠⣤⣤⣤⣤⣠⣀⣀⠀⠀⠀⠈⠙⠻⣿⣿⣷⠀
⢠⣿⣿⣿⣿⡿⠿⠟⠛⠛⠛⠛⠛⠘⠺⠿⢿⣿⣶⣤⣀⣠⣿⣿⣿⡄
⢸⣿⣿⣿⣿⣇⣀⣀⣤⣤⣤⣤⣤⣄⣀⣀⠀⠀⠉⠛⢿⣿⣿⣿⣿⡇
⠘⣿⣿⣿⣿⣿⠿⠿⠛⠛⠛⠛⠛⠛⠿⠿⣿⣶⣦⣤⣾⣿⣿⣿⣿⠃
⠀⢿⣿⣿⣿⣿⣤⣤⣤⣤⣶⣶⣦⣤⣤⣄⡀⠈⠙⣿⣿⣿⣿⣿⡿⠀
⠀⠈⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣾⣿⣿⣿⣿⡿⠁⠀
⠀⠀⠀⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠀⠀⠀
⠀⠀⠀⠀⠈⠛⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠛⠁⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠈⠙⠛⠛⠿⠿⠿⠿⠛⠛⠋⠁⠀⠀⠀⠀⠀⠀⠀

'''

Write.Print(f"{banner}", Col.DynamicMIX((Col.green, Col.black)) 
, interval=0)


options = Options()
options.page_load_strategy = 'eager'
options.headless = False
options.add_argument('--disable-blink-features=AutomationControlled')
options.add_argument('--disable-blink-features=AutomationControlled')
options.add_argument("--log-level=OFF")
options.add_experimental_option("detach", True)
options.add_experimental_option('excludeSwitches', ['enable-logging'])





## open required files for credentials
with open("username.txt", "r") as username_file, open("password.txt", "r") as password_file:
    username_line = username_file.readlines()
    password_line = password_file.readlines()


while True:
    driver = webdriver.Chrome(options=options) ## Initialise the driver
    driver.get("https://accounts.spotify.com/en/login?continue=https%3A%2F%2Fopen.spotify.com%2F") ## login to Spotify
## driver.maximize_window()
    wait = WebDriverWait(driver, 100)   
    ## Username
    username_field = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/div/div/div[1]/div[1]/input')
    username_field.clear()
    for lines in username_line:
        username_field.send_keys(lines)

    ## password

    password_field = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/div/div/div[1]/div[2]/div[2]/input')
    password_field.clear()
    for lines in password_line:
        password_field.send_keys(lines)


    ## login
    login_button = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/div/div/div[1]/div[4]/button').click()


    sleep(4)

## cookies

    driver.find_element(By.XPATH, '/html/body/div[13]/div[3]/div/div[1]/div/div[2]/div/button[1]').click()

## Search

## driver.find_element(By.XPATH, '/html/body/div[4]/div/div[2]/div[2]/nav/div[1]/ul/li[2]').click()

    driver.get('https://open.spotify.com/user/ahmeddanial')

    sleep(4)

## Follow
    driver.find_element(By.XPATH, "/html/body/div[4]/div/div[2]/div[4]/div[1]/div[2]/div[2]/div/div/div[2]/main/section/div/div[3]/div[4]/div/div/div/div/button[1]").click()

    driver.get("https://open.spotify.com/logout")