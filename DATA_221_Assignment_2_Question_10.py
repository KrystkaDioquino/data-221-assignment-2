#Defines a function that takes in the file name and a keyword to find lines containing it.
def find_lines_containing(file_name, keyword_to_find):

    #Converts the keyword to lowercase
    keyword_in_lowercase = keyword_to_find.lower()

    #Creates an empty list where the lines found will be stored
    list_of_lines_with_the_keyword = []

    #This opens and read the file
    with open(file_name, "r") as file_to_check:

        #This loops through all the lines in the file and check for words that matches the keyword
        for line_number, line_text in enumerate(file_to_check, 1):

            #Converts the lines to lowercase same as the keyword
            line_text = line_text.lower()

            #Checks if the specific line contains the keyword and appends the line number and content to the list if found
            if keyword_in_lowercase in line_text:
                line_with_the_keyword = (line_number, line_text.strip())
                list_of_lines_with_the_keyword.append(line_with_the_keyword)

    #Returns the list of all matching lines
    return list_of_lines_with_the_keyword

#Allows user to input a keyword
keyword_to_find = input("Enter your keyword: ")

#Calls the function
lines_containing_keyword = find_lines_containing("sample-file.txt", keyword_to_find)

#Gets the total number of lines with the keyword
number_of_lines_with_keyword = len(lines_containing_keyword)

#Displays the total number of matching lines
print(f"The number of matching lines found: {number_of_lines_with_keyword}")

#This checks if there are matching lines and displays proper message.
if number_of_lines_with_keyword > 0:

    #Gets the first three matching lines
    first_three_matching_lines = lines_containing_keyword[:3]
    print("These are the first three matching lines:")

    #Prints out all first three matching lines
    for matching_lines in first_three_matching_lines:
        print(matching_lines)
