import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

try:
    # Send GET request to the URL
    response = requests.get('https://www.cityofsanrafael.org/major-planning-projects-2/')
    response.raise_for_status()  # Raise an exception for unsuccessful HTTP response codes

    # Parse HTML content using BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')
    text=soup.find('div',class_='panel-widget-style panel-widget-style-for-55564-0-0-2')
    print(text)
    table=text.find('table',class_='table')
    # time.sleep(5)
    # table=text.find('table')
    print(table.text)

    # Convert table to DataFrame
    df = pd.read_html(str(table))[0]  # Use [0] because read_html returns a list of DataFrames

    # Write DataFrame to Excel
    df.to_excel('./Excel/cityOfSanrafael.xlsx', index=False)

except requests.exceptions.RequestException as e:
    print(f"Error: {e}")