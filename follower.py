import requests
import string
import random
import argparse
import sys
from pystyle import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from time import sleep
import os
import ctypes


def set_terminal_title(title):
    ctypes.windll.kernel32.SetConsoleTitleW(title)

followers_count = 0


while True:
    def generate_random_string(length):
        characters = string.ascii_lowercase + string.digits
        return "".join(random.choice(characters) for _ in range(length))


    def generate_random_text(length):
        return "".join(random.choice(string.ascii_lowercase) for _ in range(length))
    
    
    def generate_account():
        nickname = generate_random_text(8)
        password = generate_random_string(12)
        email = f"{nickname}@{generate_random_text(5)}.com"
    
        headers = {
            "Accept-Encoding": "gzip",
            "Accept-Language": "en-US",
            "App-Platform": "Android",
            "Connection": "Keep-Alive",
            "Content-Type": "application/x-www-form-urlencoded",
            "Host": "spclient.wg.spotify.com",
            "User-Agent": "Spotify/8.6.72 Android/29 (SM-N976N)",
            "Spotify-App-Version": "8.6.72",
            "X-Client-Id": generate_random_string(32)
        }
    
        payload = {
            "creation_point": "client_mobile",
            "gender": "male" if random.randint(0, 1) else "female",
            "birth_year": random.randint(1990, 2000),
            "displayname": nickname,
            "iagree": "true",
            "birth_month": random.randint(1, 11),
            "password_repeat": password,
            "password": password,
            "key": "142b583129b2df829de3656f9eb484e6",
            "platform": "Android-ARM",
            "email": email,
            "birth_day": random.randint(1, 20)
        }
    
        response = requests.post('https://spclient.wg.spotify.com/signup/public/v1/account/', headers=headers,
                                 data=payload)
    
        if response.status_code == 200:
            if response.json()['status'] == 1:
                return True, f"{nickname}:{response.json()['username']}:{email}:{password}"
            else:
                return False, "Could not create the account, some errors occurred"
        else:
            return False, f"Could not load the page. Response code: {response.status_code}"
    
    
    if __name__ == "__main__":
        parser = argparse.ArgumentParser()
        parser.add_argument("-n", "--number", help="how many accounts to generate, default is 1",
                            type=lambda x: (int(x) > 0) and int(x) or sys.exit("Invalid number: minimum amount is 1"))
        parser.add_argument("-o", "--output", help="output file, default prints to the console")
        args = parser.parse_args()
    
        number_of_accounts = args.number if args.number else 1
        output_file = open(args.output, "a") if args.output else sys.stdout
    
        print("Generating accounts in the following format:")
        print("NICKNAME:USERNAME:EMAIL:PASSWORD\n")
    
        for _ in range(number_of_accounts):
            result = generate_account()
            if result[0]:
                account_info = result[1]
                print(account_info, file=output_file)
                if output_file is not sys.stdout:
                    print(account_info, file=sys.stdout)
    
                nickname, username, email, password = account_info.split(":")
    
                #with open("email.txt", "a") as email_file:
                 #   email_file.write(email + "\n")
                with open("./ACC/username.txt", "a") as username_file:
                    username_file.write(username + "\n")
                #with open("nickname.txt", "a") as nickname_file:
                 #   nickname_file.write(nickname + "\n")
                with open("./ACC/password.txt", "a") as password_file:
                    password_file.write(password + "\n")
    
                os.system('cls')
    
                banner = '''
    
                ⠀⠀⠀⠀⠀⠀⠀⢀⣠⣤⣤⣶⣶⣶⣶⣤⣤⣄⡀⠀⠀⠀⠀⠀⠀⠀
                ⠀⠀⠀⠀⢀⣤⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣤⡀⠀⠀⠀⠀
                ⠀⠀⠀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⠀⠀⠀
                ⠀⢀⣾⣿⡿⠿⠛⠛⠛⠉⠉⠉⠉⠛⠛⠛⠿⠿⣿⣿⣿⣿⣷⡀⠀
                ⠀⣾⣿⣿⣇⠀⣀⣀⣠⣤⣤⣤⣤⣠⣀⣀⠀⠀⠀⠈⠙⠻⣿⣿⣷⠀
                ⢠⣿⣿⣿⣿⡿⠿⠟⠛⠛⠛⠛⠛⠘⠺⠿⢿⣿⣶⣤⣀⣠⣿⣿⣿⡄
                ⢸⣿⣿⣿⣿⣇⣀⣀⣤⣤⣤⣤⣤⣄⣀⣀⠀⠀⠉⠛⢿⣿⣿⣿⡇
                ⠘⣿⣿⣿⣿⣿⠿⠿⠛⠛⠛⠛⠛⠛⠿⠿⣿⣶⣦⣤⣾⣿⣿⣿⠃
                ⠀⢿⣿⣿⣿⣿⣤⣤⣤⣤⣶⣶⣦⣤⣤⣄⡀⠈⠙⣿⣿⣿⣿⡿⠀
                ⠀⠈⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣾⣿⣿⣿⣿⡇
                ⠀⠀⠀⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠀⠀⠀
                ⠀⠀⠀⠀⠀⠈⠛⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠛⠁⠀⠀⠀⠀

                        By unofficialdxnny
                '''
    
                Write.Print(f"{banner}", Col.DynamicMIX((Col.green, Col.black)), interval=0)
    
                options = Options()
                options.page_load_strategy = 'eager'
                ## options.add_argument("--headless")
                options.add_argument('--disable-blink-features=AutomationControlled')
                options.add_argument('--disable-blink-features=AutomationControlled')
                options.add_argument("--log-level=OFF")
                options.add_experimental_option("detach", True)
                options.add_experimental_option('excludeSwitches', ['enable-logging'])
    
                ## open required files for credentials
                with open("./ACC/username.txt", "r") as username_file, open("./ACC/password.txt", "r") as password_file:
                    username_line = username_file.readlines()
                    password_line = password_file.readlines()
    
                while True:
                    driver = webdriver.Chrome(options=options) ## Initialise the driver
                    driver.get("https://accounts.spotify.com/en/login?continue=https%3A%2F%2Fopen.spotify.com%2F") ## login to Spotify
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
                    sleep(2)
    
                    ## cookies
                    driver.find_element(By.XPATH, '/html/body/div[13]/div[3]/div/div[1]/div/div[2]/div/button[1]').click()
    
                    ## Search
                    driver.get(f'https://open.spotify.com/user/ahmeddanial')
                    sleep(2)
    
                    ## Follow
                    driver.find_element(By.XPATH, "/html/body/div[4]/div/div[2]/div[4]/div[1]/div[2]/div[2]/div/div/div[2]/main/section/div/div[3]/div[4]/div/div/div/div/button[1]").click()
    
                    driver.get("https://open.spotify.com/logout")
    
                    ## Clear credentials files
                    with open("./ACC/username.txt", "w"):
                        pass
                    with open("./ACC/password.txt", "w"):
                        pass
                    
                    driver.quit()
                    # Change the terminal title to "followers | x" where x is the number of followers
                    followers_count = followers_count+1  # Replace with the actual number of followers
                    new_title = f"followers | {followers_count}"
                    set_terminal_title(new_title)
    
                    break