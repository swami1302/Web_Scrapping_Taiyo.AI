import requests
from bs4 import BeautifulSoup
import csv

# Define the URL
url = 'https://www.fluor.com/projects'

try:
    # Send a GET request to the URL
    response = requests.get(url)
    response.raise_for_status()  # Raise an exception for unsuccessful HTTP response codes

    # Parse the HTML content of the webpage
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find all elements with the specified classes
    first_elements = soup.find_all(class_='SectionHeading_sectionTitleFirst__i4c3i')
    second_elements = soup.find_all(class_='SectionHeading_sectionTitleSecond___SkZp')
    third_elements = soup.find_all(class_='BodyContent_content__thrdX')  

    # Extract the content from all elements with the specified classes
    first_content_list = [element.text.strip() for element in first_elements]
    second_content_list = [element.text.strip() for element in second_elements]
    third_content_list = [element.text.strip() for element in third_elements]

    # Open a CSV file for writing
    with open('./Excel/fluor.csv', 'w', newline='', encoding='utf-8') as csvfile:
        # Create a CSV writer object
        writer = csv.writer(csvfile)

        # Write headers to the CSV file
        writer.writerow(['Content from SectionHeading_sectionTitleFirst__i4c3i', 
                         'Content from SectionHeading_sectionTitleSecond___SkZp',
                         'Content from YourClassHere'])  # Replace 'YourClassHere' with the third class name

        # Write the content to the CSV file
        max_rows = max(len(first_content_list), len(second_content_list), len(third_content_list))
        for i in range(max_rows):
            first_content = first_content_list[i] if i < len(first_content_list) else ''
            second_content = second_content_list[i] if i < len(second_content_list) else ''
            third_content = third_content_list[i] if i < len(third_content_list) else ''
            writer.writerow([first_content, second_content, third_content])

    print('Data successfully scraped and saved to content_with_all_classes.csv')

except requests.exceptions.RequestException as e:
    print(f"Error: {e}")
