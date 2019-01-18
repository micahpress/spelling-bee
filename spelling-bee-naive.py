import os

# Main method, finds the valid words for today.
def main():
    # Prompts the user for the path to the dictionary.
    path_to_dict = input("What is the path to the dictionary? ")
    path_to_dict = os.fspath(path_to_dict)
    
    # Prompts the user for the set of letters in today's game.
    set_size = 0
    while set_size is not 7:
        letters = input("What are the letters today? (Separate with spaces please): ")
        letters = letters.lower()
        letters = letters.split(" ")
        set_size = len(letters)
    letters.sort()
    
    # Prompts the user for the key letter for today.
    let_size = 0
    while let_size is not 1:
        key_let = input("What is the middle letter today? ")
        let_size = len(key_let)

    # Opens the dictionary and iterates through it, testing each word for the
    # validity conditions. If the word is valid, it prints.
    with open(path_to_dict) as sample_dict:
        for word in sample_dict:
            word = word[:len(word) - 1]

            i = 0
            contains_key = False

            if not word.isalpha():
                break

            if len(word) >= 4:
                while i < len(word):
                    if word[i] in letters:
                        if word[i] is key_let:
                            contains_key = True
                        i = i + 1
                    else:
                        break
                
                if contains_key and i is len(word):
                    print (word)

if __name__ == "__main__":
    main()