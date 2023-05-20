import requests
import string
import random
import argparse
import sys


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

            with open("email.txt", "a") as email_file:
                email_file.write(email + "\n")
            with open("username.txt", "a") as username_file:
                username_file.write(username + "\n")
            with open("nickname.txt", "a") as nickname_file:
                nickname_file.write(nickname + "\n")
            with open("password.txt", "a") as password_file:
                password_file.write(password + "\n") 
