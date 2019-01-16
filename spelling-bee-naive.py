import os

def main():
    path_to_dict = input("What is the path to the dictionary? ")
    path_to_dict = os.fspath(path_to_dict)
    
    set_size = 0
    while set_size is not 7:
        letters = input("What are the letters today? (Separate with spaces please): ")
        letters = letters.lower()
        letters = letters.split(" ")
        set_size = len(letters)
    letters.sort()
    
    let_size = 0
    while let_size is not 1:
        key_let = input("What is the middle letter today? ")
        let_size = len(key_let)

    with open(path_to_dict) as sample_dict:
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
                    print (word)

if __name__ == "__main__":
    main()