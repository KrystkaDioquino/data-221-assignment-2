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

#Finds the title of the page with the <title> tag. At first it doesn't work but with the help of the headers, I successfully found the title.
wikipedia_page_title = parsed_wikipedia_html_document.find("title").get_text()
print(wikipedia_page_title)

#This finds the main text content using the provided specific divider and id
wikipedia_content = parsed_wikipedia_html_document.find("div", id = "mw-content-text")

#Gets all the paragraph content with the p tag
all_paragraph_content = wikipedia_content.find_all("p")

#This is the variable that stores the first valid paragraph found using the for loop
first_valid_paragraph_content = ""

#Loops through each paragraph found in the all_paragraph_content and looks for the first one with at least 50 characters
for paragraph_content in all_paragraph_content:
    paragraph_text = paragraph_content.get_text(" ", strip = True)
    if len(paragraph_text) >= 50:
        first_valid_paragraph_content = paragraph_text
        break

#Prints the valid paragraph
print(first_valid_paragraph_content)







