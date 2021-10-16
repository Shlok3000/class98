def countWordsFromFile():
    filename = input("Please Enter the file name: ")
    file = open(filename, "r")
    countWords = 0
    for line in file:
        words = line.split()
        countWords = countWords + len(words)
    print("Number of word in the file", countWords)
countWordsFromFile()