
def readBook():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        print(file_contents)

def wordCount():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        wordCount = file_contents.split()
        print(len(wordCount), " words found in this document")

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
        return(letters_dict)

# def dictNum(dict):
#     return dict.values()

def sortMe(dict):
    # unsortedDict = letterCount()
    # unsortedDict.sort(reverse=True, key=dictNum)
    # print(unsortedDict)
    
    


    pass


def main():
    print("=== Begin report of books/frankenstein.txt ===")
    wordCount()

    print("=== End of report ===")

main()

