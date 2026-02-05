#This opens and read the sample text file
with (open("sample-file.txt", "r") as file):
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

    #Creates an empty dictionary where the bigrams and its frequency will be stored
    bigramsCreated = {}

    for i in range(len(processedWordsWithAtLeastTwoCharacters)):

        #This gets the first and second word and make a bigram with it.
        firstWordOfTheBigram = processedWordsWithAtLeastTwoCharacters[i-1]
        secondWordOfTheBigram = processedWordsWithAtLeastTwoCharacters[i]

        bigram = firstWordOfTheBigram + " " + secondWordOfTheBigram

        #Counts the total number of times the bigram has appeared or made
        if bigram in bigramsCreated:
            bigramsCreated[bigram] = bigramsCreated[bigram] + 1
        else:
            bigramsCreated[bigram] = 1


    #This sorts the bigrams (key) by their value
    sortedBigramsByFrequencies = sorted(bigramsCreated.items(), key = lambda x: x[1], reverse=True)

    #Gets only the top five most frequent bigram
    topFiveBigram = sortedBigramsByFrequencies[:5]

    #The for loop that neatly displays the bigram(key) and their count(value) in descending order
    for frequentBigram, frequentBigramCount in topFiveBigram:
        print(f"{frequentBigram} -> {frequentBigramCount}")

