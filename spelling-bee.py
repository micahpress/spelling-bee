import os

class Node:
    def __init__(self, word, is_terminal):
        self.word = word
        self.size = len(word)
        self.children = {}
        self.terminal = is_terminal

    def insert(self, word):
        left = word[self.size:]
        if len(left) is 1:
            if left not in self.children:
                to_insert = Node(word, True)
                self.children[left] = to_insert
            else:
                self.children.get(left).make_terminal()
        elif len(left) > 1:
            first = left[0]
            if first in self.children:
                self.children.get(first).insert(word)
            else:
                intermed = Node(word[:self.size + 1], False)
                intermed.insert(word)
                self.children[first] = intermed
    
    def recur_print(self):
        if self.terminal:
            print (self.word)
        for k in self.children:
            self.children.get(k).recur_print()
    
    def make_terminal(self):
        self.terminal = True
    
    def find_words(self, min_len, max_len, let_set, key_let):
        if key_let in self.word:
            if self.terminal:
                if self.size >= min_len and self.size < max_len:
                    print (self.word)
        if self.size < max_len:
            for letter in let_set:
                if letter in self.children:
                    self.children.get(letter).find_words(min_len, max_len, let_set, key_let)

def main():
    path_to_dict = input("What is the path to the dictionary? ")
    if path_to_dict is not '':
        path_to_dict = os.fspath(path_to_dict)
    else: 
        path_to_dict = os.fspath("./dictionaries/master-sorted.txt")

    root = Node("", False)

    with open(path_to_dict) as sample_dict:
        for word in sample_dict:
            if word[len(word) - 3] is '\'':
                word = word[:len(word) - 3]
            else:
                word = word[:len(word) - 1]
            word = word.lower()
            root.insert(word)

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
    
    length = 0
    while length < 4:
        length = input("What would you like the maximum word length to be? ")
        if length is not '':
            length = int(length)
        else:
            length = 20

    root.find_words(4, length, letters, key_let)

if __name__ == "__main__":
    main()