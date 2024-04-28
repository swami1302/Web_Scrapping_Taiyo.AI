import requests
from bs4 import BeautifulSoup
# import openai

# Set up OpenAI API
# openai.api_key = 'YOUR_OPENAI_API_KEY'

def traditional_scraping(url):
    try:
        # Send GET request to the URL
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for unsuccessful HTTP response codes

        # Parse HTML content using BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extract project titles and descriptions
        projects = []
        for project in soup.find_all('div', class_='rich-text'):
            # title = project.find('h1').text.strip()
            description = project.find('p').text.strip()
            projects.append({'title': "Construction", 'description': description})

        return projects

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None

def language_model_scraping(text):
    try:
        # Use OpenAI API to interpret unstructured data
        response = openai.Completion.create(
            engine="davinci",
            prompt=text,
            max_tokens=100
        )

        # Extract relevant information from OpenAI response
        projects = []
        for result in response['choices']:
            title = result['text'].split('\n')[0].strip()
            description = result['text'].split('\n')[1].strip()
            projects.append({'title': title, 'description': description})

        return projects

    except Exception as e:
        print(f"Error: {e}")
        return None

def main():
    # Example URL for traditional web scraping
    url = 'https://dot.ca.gov/programs/procurement-and-contracts/bid-opportunities'

    # Example text for language model-based scraping
    text = """Generate project titles and descriptions from unstructured text using the OpenAI API."""

    # Traditional web scraping
    traditional_projects = traditional_scraping(url)
    if traditional_projects:
        print("Projects scraped using traditional web scraping:")
        for project in traditional_projects:
            print(project)

    # # Language model-based scraping
    # language_model_projects = language_model_scraping(text)
    # if language_model_projects:
    #     print("\nProjects generated using language model-based scraping:")
    #     for project in language_model_projects:
    #         print(project)

if __name__ == "__main__":
    main()
