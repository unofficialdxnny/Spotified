
# Spotified

This Python script automates the process of creating multiple Spotify accounts. It uses Selenium to interact with the Spotify signup page, filling in user details such as email, password, display name, and date of birth.

## Table of Contents
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [How the Code Works](#how-the-code-works)
- [Entering Spotify URL](#entering-spotify-url)
- [ChromeDriver Installation](#chromedriver-installation)
- [Contributing](#contributing)

## Requirements
- Python 3.x
- Selenium library
- JSON files containing first and last names

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/unofficialdxnny/Spotified.git
   cd Spotified
   ```

2. **Install required Python libraries:**
   ```bash
   pip install selenium
   ```

3. **Download ChromeDriver:**
   - Visit the [ChromeDriver download page](https://chromedriver.chromium.org/downloads).
   - Select the version that matches your installed Chrome version (you can check your Chrome version by going to `chrome://settings/help`).
   - Download the appropriate executable for your OS (Windows, Mac, Linux).
   - Place the `chromedriver.exe` file in the root directory of the project.

## Usage
1. Ensure you have the `firstnames.json` and `lastnames.json` files in the `data` directory, containing first and last names respectively.
2. Update the code with your Spotify profile or playlist URL (see instructions below).
3. Run the script:
   ```bash
   python main.py
   ```
4. The script will run in a loop, creating Spotify accounts and saving the details to `account_details.txt` in the `data/accounts` directory.

## How the Code Works
- The script starts by importing necessary libraries and defining functions.
- It loads first and last names from JSON files and sets up a Chrome browser instance using Selenium.
- Random names, emails, and dates of birth are generated.
- The script navigates to the Spotify signup page and fills out the form using the generated details.
- Once an account is created, it navigates to a specified URL (either your Spotify profile or a playlist).
- Account details are saved in a text file for future reference.

## Entering Spotify URL
To make the script navigate to your Spotify profile or playlist after creating an account, follow these steps:

1. Open the `main.py` file in a text editor.
2. Find the section where the script navigates to a URL. It will look something like this:
   ```python
   driver.get('https://open.spotify.com/playlist/your_playlist_id')
   ```
3. Replace the URL in quotes with the URL of your desired Spotify profile or playlist.
   - For a playlist, it will look like: `https://open.spotify.com/playlist/your_playlist_id`
   - For a profile, it will look like: `https://open.spotify.com/user/your_profile_id`
4. Save the file.

## ChromeDriver Installation
To install ChromeDriver for your specific version of Chrome:

1. **Check your Chrome version:**
   - Open Chrome and go to `chrome://settings/help` to find your version number.

2. **Download the matching ChromeDriver:**
   - Visit the [ChromeDriver downloads page](https://chromedriver.chromium.org/downloads).
   - Click on the version that matches your Chrome version.
   - Download the appropriate file for your operating system.

3. **Extract and place the executable:**
   - Extract the downloaded file (if compressed) and place the `chromedriver.exe` in the root directory of your project.

## Contributing
Contributions are welcome! If you have suggestions for improvements or encounter any issues, please open an issue or submit a pull request.

---

**Disclaimer:** This script is intended for educational purposes only. Please ensure that your use of this script complies with Spotify's terms of service.
