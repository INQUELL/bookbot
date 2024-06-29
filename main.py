
def readBook():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        print(file_contents)

def wordCount():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        wordCount = file_contents.split()
        print(len(wordCount))

def characterCount():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        file_lower = file_contents.lower()
        letters_lower = {file_lower}
        print(letters_lower)

def main():
    characterCount()
    pass

main()

