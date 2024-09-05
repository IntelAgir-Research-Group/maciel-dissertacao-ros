import requests
from bs4 import BeautifulSoup

def extract_issue_links(url):
    # Send a request to fetch the webpage content
    response = requests.get(url)
    
    # Check if the request was successful
    if response.status_code != 200:
        print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
        return []

    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find all elements with the class 'issue-link'
    issue_links = soup.find_all(class_='issue-link')

    # Create a list to store the extracted data
    issues = []

    # Loop through each 'issue-link' element
    for link in issue_links:
        description = link.text.strip()
        href = link.get('href')
        issues.append({'description': description, 'url': href})

    return issues

# Example usage
url = 'https://github.com/ros2/ros2/issues/607'  # Replace with your target URL
issues = extract_issue_links(url)

# Print the extracted issues
if issues:
    for i, issue in enumerate(issues, start=1):
        print(f"Issue {i}:")
        print(f"Description: {issue['description']}")
        print(f"URL: {issue['url']}\n")
else:
    print("No issues found.")

