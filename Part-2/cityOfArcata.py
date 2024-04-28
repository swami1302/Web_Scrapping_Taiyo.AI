import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

try:
    # Send GET request to the URL
    response = requests.get('https://www.cityofarcata.org/413/Current-City-Construction-Projects')
    response.raise_for_status()  # Raise an exception for unsuccessful HTTP response codes

    # Parse HTML content using BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')
    text=soup.find('div',id='cc8bd95fde-da5f-45d7-9e90-d6e2eb24437f')
    print(text)
    # text1=text.find('div',class_='widgetBody')
    # time.sleep(5)
    table=text.find('table')
    print(table.text)

    # Convert table to DataFrame
    df = pd.read_html(str(table))[0]  # Use [0] because read_html returns a list of DataFrames

    # Write DataFrame to Excel
    df.to_excel('./Excel/cityOfArcata.xlsx', index=False)

except requests.exceptions.RequestException as e:
    print(f"Error: {e}")