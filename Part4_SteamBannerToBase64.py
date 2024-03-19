import os
import csv
import base64

# Define the paths to the game_images folder and the CSV file
image_folder = "game_images"
csv_file = "steamgameswithgenre.csv"

# Open the CSV file for reading and writing
with open(csv_file, 'r', newline='') as file:
    reader = csv.DictReader(file)
    rows = list(reader)
    fieldnames = reader.fieldnames  # Store the fieldnames in a variable
    
    # Print the fieldnames
    print("Fieldnames:", fieldnames)

# Iterate over the rows in the CSV file
for row in rows:
    if 'AppID' in row and row['AppID']:
        app_id = row['AppID']
        image_path = os.path.join(image_folder, f"{app_id}.jpg")

        # Check if the image file exists
        if os.path.exists(image_path):
            # Open the image file in binary mode and read its contents
            with open(image_path, 'rb') as image_file:
                image_data = image_file.read()

            # Convert the image data to base64
            base64_image = base64.b64encode(image_data).decode('utf-8')

            # Update the 'Base64 Image' column in the CSV file
            row['Base64 Image'] = base64_image
            
# Print the first 5 rows
for i, row in enumerate(rows):
    if i >= 5:  # Only print the first 5 rows
        break
    print(row)

# Write the updated rows back to the CSV file
with open(csv_file, 'w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=fieldnames)  # Use the updated fieldnames
    writer.writeheader()
    writer.writerows(rows)