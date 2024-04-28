import requests
from bs4 import BeautifulSoup
import pandas as pd

try:
    # Send GET request to the URL
    response = requests.get('https://dot.ca.gov/programs/procurement-and-contracts/bid-opportunities')
    response.raise_for_status()  # Raise an exception for unsuccessful HTTP response codes

    # Parse HTML content using BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')
    text=soup.find('div',class_='table-responsive')
    table=text.find('table',class_='table')
    print(table.text.strip())

    # Convert table to DataFrame
    df = pd.read_html(str(table))[0]  # Use [0] because read_html returns a list of DataFrames

    # Write DataFrame to Excel
    df.to_excel('./Excel/caltrans.xlsx', index=False)

except requests.exceptions.RequestException as e:
    print(f"Error: {e}")