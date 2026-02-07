sets_of_duplicates = {}

#This opens the file
with open("sample-file.txt", "r") as file_to_check:

    #Loop through the file
    for line_number, line_text in enumerate(file_to_check, 1):

        #Keeps the original text for printing later
        original_text = line_text.strip()

        #Convert to lowercase and clean it for comparison
        cleaned_text = "".join(char.lower() for char in original_text if char.isalnum())

        #This skips any empty lines
        if not cleaned_text:
            continue

        #If the cleaned text isn't in the dictionary yet, it creates a new list
        if cleaned_text not in sets_of_duplicates:
            sets_of_duplicates[cleaned_text] = []

        #Adds the line number and original text to the group
        sets_of_duplicates[cleaned_text].append((line_number, original_text))

#Filter for groups that have more than one line
final_duplicate_sets = []
for group in sets_of_duplicates.values():
    if len(group) > 1:
        final_duplicate_sets.append(group)

#Gets the total number of duplicate sets found
total_sets_found = len(final_duplicate_sets)

#Displays the total number of sets
print(f"Total number of near-duplicate sets: {total_sets_found}")

#This checks if there are duplicate sets and displays the first two
if total_sets_found > 0:
    print("These are the first two sets found:")

    #Slice the list to get only the first two sets
    for i, duplicate_set in enumerate(final_duplicate_sets[:2], 1):
        for line_info in duplicate_set:
            print(f"{line_info[0]} -> {line_info[1]}")