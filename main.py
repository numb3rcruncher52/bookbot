with open("books/frankenstein.txt") as f:
    file_contents = f.read()

def countWords(string):
    words = string.split()
    return(len(words))

print(countWords(file_contents))