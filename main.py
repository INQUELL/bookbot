
def readBook():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        print(file_contents)

def wordCount():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        wordCount = file_contents.split()
        print("Word count is: ", len(wordCount))

def letterCount():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        file_lower = file_contents.lower()

        letters_dict = {}

        for letter in file_lower:
            if letter in letters_dict:
                letters_dict[letter] += 1
            else:
                letters_dict[letter] = 1
        print(letters_dict)

def main():
    letterCount()
    pass

main()

