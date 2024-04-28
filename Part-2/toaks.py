import requests
from bs4 import BeautifulSoup
import csv

# Define the URL
url = 'https://www.toaks.org/departments/public-works/construction'

try:
    # Send a GET request to the URL
    response = requests.get(url)
    response.raise_for_status()  # Raise an exception for unsuccessful HTTP response codes

    # Parse the HTML content of the webpage
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find all elements with the specified classes
    first_elements = soup.find(id='widget_2536_309_504')
    # print(first_elements.text)
    # Find all <h3> and <p> elements within the first element
    headings = first_elements.find_all('h3')
    paragraphs = first_elements.find_all('p')

    # Open a CSV file for writing
    with open('./Excel/toaks.csv', 'w', newline='', encoding='utf-8') as csvfile:
        # Create a CSV writer object
        writer = csv.writer(csvfile)

        # Write headers to the CSV file
        writer.writerow(['Heading', 'Content'])

        # Iterate over <h3> elements and corresponding <p> elements
        for heading, paragraph in zip(headings, paragraphs):
            # Extract text from <h3> and <p> elements
            heading_text = heading.text.strip()
            paragraph_text = paragraph.text.strip()

            if heading_text and paragraph_text:
                writer.writerow([heading_text, paragraph_text])

    print('Data successfully scraped and saved to toaks.csv')

except requests.exceptions.RequestException as e:
    print(f"Error: {e}")
