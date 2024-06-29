
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
            if letter.isalpha(): # Removes anything that isn't a letter
                if letter in letters_dict:
                    letters_dict[letter] += 1
                else:
                    letters_dict[letter] = 1
        #return(letters_dict)
        
        # Remember, sometimes you gotta convert data between types to use them. 
        # Here, we converted the data in the list into tuples so we can sort them.
        letters_list = list(letters_dict.items())
        # Lambda is a way to make a small anonymous function on the fly
        sorted_letters = sorted(letters_list, reverse=True, key=lambda x: x[1])
        print(sorted_letters)


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
    letterCount()
    print("=== End of report ===")

main()

