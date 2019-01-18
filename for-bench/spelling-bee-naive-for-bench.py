import os

def find_words(sample_dict, letters, key_let):
    for word in sample_dict:
        word = word[:len(word) - 1]

        i = 0
        contains_key = False

        if len(word) >= 4:
            while i < len(word):
                if word[i] in letters:
                    if word[i] is key_let:
                        contains_key = True
                    i = i + 1
                else:
                    break
            
            if contains_key and i is len(word):
                # print (word)
                pass

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
