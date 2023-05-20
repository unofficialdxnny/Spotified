import requests
import random
import string


def generate_random_string(length):
    characters = string.ascii_lowercase + string.digits
    return "".join(random.choice(characters) for _ in range(length))


def follow_user(username, password, user_id):
    # Authenticate with Spotify
    auth_response = requests.post('https://accounts.spotify.com/api/token', data={
        'grant_type': 'password',
        'username': username,
        'password': password,
        'client_id': "8b4bf7a55fc54b9d81c86e7c17840f16",
        'client_secret': "2af9f62f91d2493787432a1227bc87e2"
    })

    if auth_response.status_code != 200:
        print('Authentication failed')
        return

    access_token = auth_response.json().get('access_token')

    # Follow the user
    follow_response = requests.put(f'https://api.spotify.com/v1/me/following?type=user&ids={user_id}', headers={
        'Authorization': f'Bearer {access_token}',
        'Content-Type': 'application/json'
    })

    if follow_response.status_code == 204:
        print(f'Successfully followed user with ID: {user_id}')
    else:
        print('Failed to follow user')

# Replace with your Spotify username, password, and the user ID you want to follow
your_username = '31hdfr2p7t3pmsfwphl4g4t3p7te'
your_password = '3q5cy3xfm3zo'
user_to_follow_id = 'ahmeddanial'

follow_user(your_username, your_password, user_to_follow_id)
