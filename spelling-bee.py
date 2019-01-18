import os

# This is a class I've written for the nodes in my trie. The constructor variables are the string
# representing the word itself and a boolean declaring whether this node is the end of the word. The
# length of the word is stored and a map to its children is also created. The node class has the self-
# methods for construction, insertion, printing, making terminal, and finding words for use in the 
# Spelling Bee game.
class Node:
    # Constructor method taking in the node's word, as a string, and a boolean describing whether this
    # node is at the end of a complete word. The word's length is stored and a map to the node's
    # children is initialized.
    def __init__(self, word, is_terminal):
        self.word = word
        self.size = len(word)
        self.children = {}
        self.terminal = is_terminal

    # Inserts the string passed in as "word" into this node's subtree.
    def insert(self, word):
        # The string that still needs to be inserted is computed as the master word's length minus this
        # node's string's length.
        left = word[self.size:]
        # If there is only one letter left and it does not exist as a child of this node, it is inserted
        # as a terminal node. If it does exist (for instance if "app" was inserted after "application"), 
        # that child node is marked as terminal.
        if len(left) is 1:
            if left not in self.children:
                to_insert = Node(word, True)
                self.children[left] = to_insert
            else:
                self.children.get(left).make_terminal()
        # If there is more than 1 letter left, a node for the next letter is either inserted or followed
        # and the process recurs.
        elif len(left) > 1:
            first = left[0]
            if first in self.children:
                self.children.get(first).insert(word)
            else:
                intermed = Node(word[:self.size + 1], False)
                intermed.insert(word)
                self.children[first] = intermed
    
    # Prints this node if it's terminal, and then follows its children.
    def recur_print(self):
        if self.terminal:
            print (self.word)
        for k in self.children:
            self.children.get(k).recur_print()
    
    # Sets this node's terminal variable to true.
    def make_terminal(self):
        self.terminal = True
    
    # This is the main recursive method for finding valid words for the game. It takes in
    # a minimum word length, a maximum word length, a set of letters to choose from, and the
    # key letter of the game.
    def find_words(self, min_len, max_len, let_set, key_let):
        # If the key letter is contained in the word, the word is terminal, and it's within
        # the word length bounds, the word is valid and gets printed.
        if key_let in self.word:
            if self.terminal:
                if self.size >= min_len and self.size < max_len:
                    print (self.word)
        # If the word isn't the maximum length, This method is called on each of its valid
        # children.
        if self.size < max_len:
            for letter in let_set:
                if letter in self.children:
                    self.children.get(letter).find_words(min_len, max_len, let_set, key_let)

# Main method, runs the program.
def main():
    # Prompts the user for a path to a dictionary. If the input is left black, it defaults to
    # the dictionary I provide.
    path_to_dict = input("What is the path to the dictionary? ")
    if path_to_dict is not '':
        path_to_dict = os.fspath(path_to_dict)
    else: 
        path_to_dict = os.fspath("./dictionaries/master-sorted.txt")

    # Initializes the root node of the trie.
    root = Node("", False)

    # Constructs the trie by reading in words from the dictionary and checking that their length
    # is at least 4 and that the string is comprised of only alphabetic characters before inserting
    # it into the tree.
    with open(path_to_dict) as sample_dict:
        for word in sample_dict:
            word = word[:len(word) - 1]
            if word.isalpha():
                word = word.lower()
                root.insert(word)

    # Asks the user for the set of 7 letters used in today's Spelling Bee game.
    set_size = 0
    while set_size is not 7:
        letters = input("What are the letters today? (Separate with spaces please): ")
        letters = letters.lower()
        letters = letters.split(" ")
        set_size = len(letters)
    letters.sort()
    
    # Asks the user for the key letter for the day.
    let_size = 0
    while let_size is not 1:
        key_let = input("What is the middle letter today? ")
        let_size = len(key_let)
    
    # Asks the user to specify a maximum word length. If the input is blank, it defaults to 20.
    length = 0
    while length < 4:
        length = input("What would you like the maximum word length to be? ")
        if length is not '':
            length = int(length)
        else:
            length = 20

    # Calls the find_words method on the tree with the input from the user.
    root.find_words(4, length, letters, key_let)

if __name__ == "__main__":
    main()