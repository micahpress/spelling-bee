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
    path_to_dict = "dictionaries/combo.txt"
    path_to_dict = os.fspath(path_to_dict)

    root = Node("", False)

    with open(path_to_dict) as sample_dict:
        for word in sample_dict:
            word = word[:len(word) - 1]
            root.insert(word)

    length = 20
    letters = ['c', 'a', 'n', 'b', 'o', 'l', 'r']
    letters.sort()
    key_let = 'n'

    root.find_words(4, length, letters, key_let)

if __name__ == "__main__":
    main()
