from bs4 import BeautifulSoup
import requests

#Custom headers to avoid being blocked or showing up differently
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
    "AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/124.0.0.0 Safari/537.36"}

#Using requests library to extract the source code of the wikipedia link I provided
wikipedia_Data_Science_html = requests.get("https://en.wikipedia.org/wiki/Data_science", headers=headers).text

#This parse the HTML content using BeautifulSoup
parsed_wikipedia_html_document = BeautifulSoup(wikipedia_Data_Science_html, "html5lib")

#This finds the main text content using the provided specific divider and id
wikipedia_content = parsed_wikipedia_html_document.find("div", id = "mw-content-text")

#Gets all the <h2> section headings
all_headings_from_content = wikipedia_content.find_all("h2")

#List of words that the heading must not contain
forbidden_heading_words = ["references", "external links", "see also", "notes"]

#Stores all the valid heading text that are found using the for loop.
all_valid_heading_list = []

#Goes through all the <h2> tag
for heading in all_headings_from_content:

    #Strips out and cleans the text found
    heading_text = heading.get_text(" ", strip = True).replace("[edit]", "")

    #Converts the heading text into lowercase to compare it with the forbidden words
    lowercase_heading_text = heading_text.lower()

    #Validates the heading text if it is not in the list of forbidden heading words
    #It will then be appended into the list of valid headings
    if lowercase_heading_text not in forbidden_heading_words:
        all_valid_heading_list.append(heading_text)
    else:
        continue

#Creates a file with all the valid heading text found
with open("heading.txt", "w") as heading_file:
    for heading in all_valid_heading_list:
        heading_file.write(heading + "\n")

