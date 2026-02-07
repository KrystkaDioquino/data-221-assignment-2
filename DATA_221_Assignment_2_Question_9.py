from bs4 import BeautifulSoup
import requests
import csv

#Custom headers to avoid being blocked or showing up differently
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
    "AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/124.0.0.0 Safari/537.36"}

#Send an HTTP request to Wikipedia and get the source code
wikipedia_machine_learning_html = requests.get("https://en.wikipedia.org/wiki/Machine_learning", headers=headers).text

#Parse the HTML content using BeautifulSoup
parsed_wikipedia_html_document = BeautifulSoup(wikipedia_machine_learning_html,"html5lib")

#Find the main Wikipedia content area
wikipedia_content = parsed_wikipedia_html_document.find("div", id="mw-content-text")

#Find all tables inside the main content
wikipedia_machine_learning_tables = wikipedia_content.find_all("table")

#Variable to store the first valid table (with at least 3 rows)
valid_table = None

#Loop through all tables to find the first one with 3 or more rows
for table in wikipedia_machine_learning_tables:
    wikipedia_table_rows = table.find_all("tr")

    if len(wikipedia_table_rows) >= 3:
        valid_table = table
        break

#Continues if a valid table was found
if valid_table:
    all_rows_in_table = valid_table.find_all("tr")

    #Extract table header
    header_cells = all_rows_in_table[0].find_all(["th", "td"])
    table_header = [cell.get_text(strip=True) for cell in header_cells]

    final_table = []
    #Loop through table rows (skip header row)
    for row in all_rows_in_table[1:]:
        cells_in_table = row.find_all(["td", "th"])

        #Extract text from each cell
        row_content = [cell.get_text(strip=True) for cell in cells_in_table]

        #If row has fewer columns, pad with empty strings
        while len(row_content) < len(table_header):
            row_content.append("")

        #If row has more columns, trim it
        row_content = row_content[:len(table_header)]

        #Add the cleaned row to final data
        final_table.append(row_content)

    #Write extracted table data to a CSV file
    with open("wiki_table.csv", "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(table_header)
        writer.writerows(final_table)
