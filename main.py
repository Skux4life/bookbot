def count_words(text):
    words = text.split()
    return len(words)

def count_letters(text):
    result = {}
    for letter in text:
        if result.get(letter) == None:
            result[letter] = 1
        else:
            result[letter] += 1
    return result

with open("books/frankenstein.txt") as f:
    file_contents = f.read()
    count = count_words(file_contents)
    print(f"{count} words found in the document")
    letters = count_letters(file_contents.lower())
    lettersList = list(letters.items())
    lettersList.sort(key=lambda a: a[1], reverse=True)
    for letter in lettersList:
        if letter[0].isalpha():
            print(f"The '{letter[0]}' was found {letter[1]} times")
