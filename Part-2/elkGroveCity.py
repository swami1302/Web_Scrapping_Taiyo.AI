import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

try:
    # Send GET request to the URL
    response = requests.get('https://www.elkgrovecity.org/southeast-policy-area/development-projects')
    response.raise_for_status()  # Raise an exception for unsuccessful HTTP response codes

    # Parse HTML content using BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')
    table=soup.find('table',class_='content-table')
    # print(text)
    # # text1=text.find('div',class_='widgetBody')
    # # time.sleep(5)
    # table=text.find('table')
    print(table.text.strip())

    # Convert table to DataFrame
    df = pd.read_html(str(table))[0]  # Use [0] because read_html returns a list of DataFrames

    # Write DataFrame to Excel
    df.to_excel('./Excel/elkGroveCity.xlsx', index=False)

except requests.exceptions.RequestException as e:
    print(f"Error: {e}")