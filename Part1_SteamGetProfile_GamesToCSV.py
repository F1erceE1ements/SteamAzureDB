import requests
import csv
import pandas as pd
from getpass import getpass

# Prompt for the Steam ID and WebAPI Key
steam_id = getpass('Enter your Steam ID: ')
web_api_key = getpass('Enter your WebAPI Key: ')

# URL to get the owned games
url = f'http://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/?key={web_api_key}&steamid={steam_id}&format=json&include_appinfo=1'

# Send the GET request
response = requests.get(url)
data = response.json()

# Open the CSV file
with open('steamgames.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Name", "Playtime", "Store", "AppID", "Genre"])  # Write the header

    # Loop through each game owned by the user
    for game in data['response']['games']:
        store_url = f'http://store.steampowered.com/app/{game["appid"]}'
        writer.writerow([game['name'], game['playtime_forever'], store_url])  # Write the game data
        
# Read the CSV file into a DataFrame
df = pd.read_csv('steamgames.csv', encoding='ISO-8859-1')

# Rename the columns
df.columns = ["Name", "Playtime", "Store URL", "AppID", "Genre"]
# Add new columns with default values
df["Base64 Image"] = ""
df["Image URL"] = ""
df["Game Complete"] = ""

# Extract the AppID from the Store URL
df['AppID'] = df['Store URL'].str.split('/').str[-1]

# Write the DataFrame back to the CSV file
df.to_csv('steamgames.csv', index=False)

print('Data export complete')