import requests
import pandas as pd
import time
import os

print('Starting script...')

# Read the steamgames.csv file
df = pd.read_csv(r'C:\Users\Pierce\Downloads\steamgames.csv')

# Convert the AppIDs to strings
df['AppID'] = df['AppID'].astype(str)

# Directory to save images
image_dir = r'C:\Users\Pierce\Downloads\game_images'
os.makedirs(image_dir, exist_ok=True)

# Loop over the AppIDs
for appid in df['AppID']:
    # Skip this AppID if its image already exists
    if os.path.exists(os.path.join(image_dir, f'{appid}.jpg')) or os.path.exists(os.path.join(image_dir, f'{appid} - Manual Handling.jpg')):
        print(f'Image for AppID {appid} already exists. Skipping...')
        continue

    print(f'Processing AppID {appid}...')
    url = f'http://store.steampowered.com/api/appdetails?appids={appid}'

    success = False
    retries = 0
    while not success and retries < 3:
        try:
            response = requests.get(url, timeout=10)
            data = response.json()

            if data[appid]['success']:
                image_url = data[appid]['data']['header_image']
                image_response = requests.get(image_url, timeout=10)

                # Save the image to a file
                with open(os.path.join(image_dir, f'{appid}.jpg'), 'wb') as f:
                    f.write(image_response.content)

                print(f'Successfully downloaded image for AppID {appid}')
                success = True
            else:
                print(f'No data available for AppID {appid}. Creating manual handling file...')
                with open(os.path.join(image_dir, f'{appid} - Manual Handling.jpg'), 'w') as f:
                    pass
                break
        except (requests.Timeout, Exception) as e:
            print(f'Error getting data for AppID {appid}: {e}')
            print('Retrying...')
            retries += 1

    # Wait for 5 seconds
    time.sleep(5)

print('Script completed.')