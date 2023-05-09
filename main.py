def readText(filename):
    with open(filename) as f:
        file_contents = f.read()
    return file_contents

def countWords(string):
    words = string.split()
    return(len(words))

def countLetters(string):
    letter_counts = {}
    for letter in string.lower():
        if letter not in letter_counts:
            letter_counts[letter] = 1
        else: 
            letter_counts[letter] += 1
    return letter_counts

def sortOn(d):
    return d["num"]

def sortedLetters(letter_counts):
    sorted_letters = []
    for letter in letter_counts:
        if letter.isalpha():
            sorted_letters.append({"char":letter, "num":letter_counts[letter]})
    sorted_letters.sort(reverse=True, key=sortOn)
    return sorted_letters

def printReport(filename):
    text = readText(filename)
    word_count = countWords(text)
    letter_count = countLetters(text)
    sorted_letters = sortedLetters(letter_count)
    
    print(f"--- Begin report of {filename} ---")
    print(f"{word_count} words found in the document\n")
    for letter in sorted_letters:
        char = letter["char"]
        times = letter["num"]
        print(f"The '{char}' was found {times} times")
    print("--- End report ---")

filename = "books/frankenstein.txt"
printReport(filename)