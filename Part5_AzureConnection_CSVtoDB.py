import pandas as pd # Import the pandas library
import getpass # Import the getpass library
import urllib # Import the urllib library
from sqlalchemy import create_engine # Import the create_engine function from the sqlalchemy library

# Target the CSV file
csv_file_path = r'C:\Users\Pierce\OneDrive\Documents\Projects\Steam_Database_Creation\Python_Project_Steam_Database_Compiler_Project\steamgameswithgenre.csv'

# Read the CSV file with pandas into a DataFrame
df = pd.read_csv(csv_file_path)

# Connect to the Azure SQL Database
server              = 'steamdbtrial.database.windows.net' # Replace 'my_server_name' with your server name
database            = 'SteamDB' # Replace 'my_database_name' with your database name
username            = getpass.getpass("Enter your Azure SQL username: ") # Prompt the user to enter their username
password            = getpass.getpass("Enter your Azure SQL password: ") # Prompt the user to enter their password
driver              = "ODBC Driver 17 for SQL Server"
connection_string   = f'mssql+pyodbc://{username}:{password}@{server}/{database}?driver={urllib.parse.quote_plus(driver)}&Connection Timeout=60'


try:
    engine = create_engine(connection_string)
    print('Connection to Azure SQL Database successful.')
except Exception as e:
    print(f'Error connecting to Azure SQL Database: {e}')
    
try:
    df.to_sql('SteamGamesCollection', engine, if_exists='replace') # Replace 'my_table' with your table name
    print('Data successfully written to Azure SQL Database.')
except Exception as e:
    print(f'Error writing data to Azure SQL Database: {e}')
    
print('Script completed.')
