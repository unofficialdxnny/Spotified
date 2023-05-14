import requests, string, random, argparse, sys

def getRandomString(length): #Letters and numbers
    pool=string.ascii_lowercase+string.digits
    return "".join(random.choice(pool) for i in range(length))

def getRandomText(length): #Chars only
    return "".join(random.choice(string.ascii_lowercase) for i in range(length))

def generate():
    nick = getRandomText(8)
    passw = getRandomString(12)
    email = nick+"@"+getRandomText(5)+".com"

    headers={"Accept-Encoding": "gzip",
             "Accept-Language": "en-US",
             "App-Platform": "Android",
             "Connection": "Keep-Alive",
             "Content-Type": "application/x-www-form-urlencoded",
             "Host": "spclient.wg.spotify.com",
             "User-Agent": "Spotify/8.6.72 Android/29 (SM-N976N)",
             "Spotify-App-Version": "8.6.72",
             "X-Client-Id": getRandomString(32)}
    
    payload = {"creation_point": "client_mobile",
            "gender": "male" if random.randint(0, 1) else "female",
            "birth_year": random.randint(1990, 2000),
            "displayname": nick,
            "iagree": "true",
            "birth_month": random.randint(1, 11),
            "password_repeat": passw,
            "password": passw,
            "key": "142b583129b2df829de3656f9eb484e6",
            "platform": "Android-ARM",
            "email": email,
            "birth_day": random.randint(1, 20)}
    
    r = requests.post('https://spclient.wg.spotify.com/signup/public/v1/account/', headers=headers, data=payload)

    if r.status_code==200:
        if r.json()['status']==1:
            return (True, nick+":"+r.json()["username"]+":"+email+":"+passw)
        else:
            #Details available in r.json()["errors"]
            #print(r.json()["errors"])
            return (False, "Could not create the account, some errors occurred")
    else:
        return (False, "Could not load the page. Response code: "+ str(r.status_code))

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-n", "--number", help="how many accounts to generate, default is 1", type=lambda x: (int(x) > 0) and int(x) or sys.exit("Invalid number: minimum amount is 1"))
    parser.add_argument("-o", "--output", help="output file, default prints to the console")
    args = parser.parse_args()

    N = args.number if args.number else 1
    file = open(args.output, "a") if args.output else sys.stdout

    print("Generating accounts in the following format:")
    print("NICKNAME:USERNAME:EMAIL:PASSWORD\n")

    for i in range(N):
        result = generate()
        if result[0]:
            print(result[1], file=file)
            if file is not sys.stdout:
                print(result[1], file=sys.stdout)

            # Write email, username, nickname, and password to separate files
            email_file = open("email.txt", "a")
            username_file = open("username.txt", "a")
            nickname_file = open("nickname.txt", "a")
            password_file = open("password.txt", "a")

            nickname, username, email, password = result[1].split(":")
            email_file.write(email + "\n")
            username_file.write(username + "\n")
            nickname_file.write(nickname + "\n")
            password_file.write(password + "\n")

            email_file.close()
            username_file.close()
            nickname_file.close()
            password_file.close()

        else:
            print(str(i+1)+"/"+str(N)+": "+result[1], file=sys.stdout)

    if file is not sys.stdout: file.close()