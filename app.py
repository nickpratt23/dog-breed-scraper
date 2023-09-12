import requests
from bs4 import BeautifulSoup

# URL of the page containing the dog breeds
url = "https://www.ckc.ca/en/Choosing-a-Dog/Choosing-a-Breed/All-Dogs"  # Replace with the actual URL

# Send an HTTP GET request to the URL
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the HTML content of the page
    soup = BeautifulSoup(response.text, "html.parser")

    # Find all the div elements with the specified class
    breed_divs = soup.find_all("div", class_="post clearfix breedPost")

    # Extract breed titles from h3 elements within the divs
    breed_titles = []
    for breed_div in breed_divs:
        h3_element = breed_div.find("h3", class_="breedListing")
        if h3_element:
            breed_title = h3_element.a.text.strip()  # Get the text within the 'a' tag
            breed_titles.append(breed_title)

    # Print the extracted breed titles in the requested format
    print(",\n".join(["'" + title + "'" for title in breed_titles]))

    # Save the breed titles to a text file
    with open("ckc-breeds.txt", "w") as file:
        for title in breed_titles:
            file.write(title + "\n")

    print("Breed titles saved to 'dog_breeds.txt'")
else:
    print("Failed to retrieve the web page. Status code:", response.status_code)