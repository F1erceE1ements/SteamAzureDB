import vdf
import pandas as pd

# Parse the sharedconfig.vdf file
with open(r'C:\Program Files (x86)\Steam\userdata\34608009\7\remote\sharedconfig.vdf', 'r') as f:
    data = vdf.parse(f)

# Extract the app IDs and their corresponding genres
genres = {}
for appid, appdata in data['UserRoamingConfigStore']['Software']['Valve']['Steam']['apps'].items():
    if 'tags' in appdata:
        genres[appid] = ', '.join(appdata['tags'].values())
        print(f'AppID: {appid}, Genres: {genres[appid]}')  # Print the AppID and genres    

# Read the steamgames.csv file
df = pd.read_csv('steamgames.csv')

# Convert the AppIDs to strings
df['AppID'] = df['AppID'].astype(str)

# Add the genres to the DataFrame
df['Genre'] = df['AppID'].map(genres)

# Write the updated data to a new CSV file
df.to_csv('steamgameswithgenre.csv', index=False)