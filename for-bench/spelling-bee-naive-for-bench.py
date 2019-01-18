import os

# This file is largely commented in the original version. I won't recomment it here,
# but I'll explain my modifications to the main method down below.

def find_words(sample_dict, letters, key_let):
    for word in sample_dict:
        word = word[:len(word) - 1]

        i = 0
        contains_key = False

        if word.isalpha():
            if len(word) >= 4:
                while i < len(word):
                    if word[i] in letters:
                        if word[i] is key_let:
                            contains_key = True
                        i = i + 1
                    else:
                        break
                
                if contains_key and i is len(word):
                    pass

# I hard-coded in the path to the dictionary and valid letters so that the profiling
# script could run this on the command-line without user input. It words the same way
# as the naive version of the program.
def main():
    path_to_dict = "../dictionaries/master-sorted.txt"

    letters = ['f', 'e', 'l', 'i', 'c', 't', 'y']
    letters.sort()
    key_let = 'f'

    sample_dict = open(path_to_dict)

    find_words(sample_dict, letters, key_let)

    sample_dict.close()

if __name__ == "__main__":
    main()
