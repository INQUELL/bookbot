
def readBook():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        print(file_contents)

def wordCount():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        wordCount = file_contents.split()
        print("Word count is: ", len(wordCount))

def characterCount():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        file_lower = file_contents.lower()
        letters_count = {}
        letter_num = 0
        for letter in file_lower:
            
            letter_num += 1
            letters_count[letter] = letter_num
        print("Letter count is: ", letters_count)

def main():
    wordCount()
    characterCount()
    pass

main()

