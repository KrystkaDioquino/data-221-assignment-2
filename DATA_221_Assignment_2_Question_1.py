#This opens and read the sample text file
with open("sample-file.txt", "r") as file:
    sampleFileContent = file.read()

    #Splits the lines into words
    sampleFileWords = sampleFileContent.split()

    #Creates an empty list for the valid words to be added
    processedWordsWithAtLeastTwoCharacters =[]

    #This loops through every word in the file
    for word in sampleFileWords:

        #Converts the word in lowercase and removes all punctuations
        processedWord = word.lower().strip()

        #Gets the length of the alphabetic number in the word
        lengthOfAlphabeticCharacterInWord = sum(character.isalpha() for character in processedWord)

        #Checks if the word has at least two alphabetic character
        if lengthOfAlphabeticCharacterInWord >= 2:
            processedWordsWithAtLeastTwoCharacters.append(processedWord)
        else:
            continue

    #Creates an empty dictionary where the valid words and its frequency will be stored
    wordCounts = {}

    #Counts the total number of times the word has appeared in the text
    for word in processedWordsWithAtLeastTwoCharacters:
        if word in wordCounts:
            wordCounts[word] = wordCounts[word] + 1
        else:
            wordCounts[word] = 1

    #This sorts the words (key) by their value
    sortedWordsByFrequencies = sorted(wordCounts.items(), key = lambda x: x[1], reverse=True)

    #Gets only the top ten most frequent word
    topTenFrequentWords = sortedWordsByFrequencies[:10]

    #The for loop that neatly displays the words(key) and their count(value) in descending order
    for frequentWord, frequentWordCount in topTenFrequentWords:
        print(f"{frequentWord} -> {frequentWordCount}")


