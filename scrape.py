import requests
from bs4 import BeautifulSoup
import csv

# URL of the Wikipedia page
url = "https://en.wikipedia.org/wiki/Lists_of_schools_in_the_United_States"

# Send an HTTP request to fetch the page content
response = requests.get(url)

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.content, "html.parser")

# Find the relevant section containing school information
school_section = soup.find("div", {"class": "div-col columns column-width"})

# Initialize lists to store school names and coordinates
school_names = []
school_coordinates = []

# Extract school names and coordinates
for row in school_section.find_all("li"):
    school_name = row.text.strip()
    school_names.append(school_name)

    # Assuming coordinates are in the format "lat, lng"
    # You may need to adjust this based on the actual data structure
    coordinates = row.find("span", {"class": "geo-dec"}).text.strip()
    school_coordinates.append(coordinates)

# Create a CSV file and write the data
with open("schools.csv", "w", newline="") as csvfile:
    fieldnames = ["name of schools", "lat", "lng"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    for name, coord in zip(school_names, school_coordinates):
        lat, lng = coord.split(", ")
        writer.writerow({"name of schools": name, "lat": lat, "lng": lng})

print("Data successfully scraped and saved to schools.csv")
