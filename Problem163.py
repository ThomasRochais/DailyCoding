from typing import Tuple

class TrieNode(object):


    def __init__(self, char: str):
        self.char = char
        self.children = []
        self.word_finished = False # Is it the last character of the word
        self.counter = 1 # How many times this character appeared in the addition process

# Adding a word in the Trie structure:
def add_word(root, word: str):
    node = root
    for char in word:
        found_in_child = False
        # Search for the character in the children of the present 'node'
        for child in node.children:
            if child.char == char:
                # We found it, so increase the counter by 1 to keep track
                # that another word has it as well
                child.counter += 1
                # and point the  node to the child that contains this char
                node = child
                found_in_child = True
                break
        # We did not find it so add a new child
        if not found_in_child:
            new_node = TrieNode(char)
            node.children.append(new_node)
            node = new_node # and point node to the new child
    # Everything is finished, so mark it as the end of a word_finished
    node.word_finished = True

def add_list(root, lst):
    for word in lst:
        add_word(root, word)

def find_prefix(root, prefix: str) -> Tuple[bool, int]:
    """
    Check and return
    1. If the prefix exists in any of the words we added so far
    2. If yes then how many words actually have the prefix
    """
    node = root
    # If the root node has no children, then return False
    # because it means we are trying to search in an empty trie
    if not root.children:
        return False, 0
    for char in prefix:
        char_not_found = True
        # Search through all the children of the present 'node'
        for child in node.children:
            if child.char == char:
                char_not_found = False # We cound the char existing in the child
                node = child # Assign node as the child containing the char and break
                break
        if char_not_found:
            return False, 0
    return True, node.counter

def words_in_trie(root):
    lst = []
    if root.children:
        for child in root.children:
            for s in words_in_trie(child):
                lst.append(child.char + s)
    else:
        lst.append("")
    return lst

def shortest_unique_prefixes(root):
    lst = []
    if root.children:
        for child in root.children:
            if child.counter > 1:
                for s in shortest_unique_prefixes(child):
                    lst.append(child.char + s)
            else:
                lst.append(child.char)
    else:
        lst.append("")
    return lst
    
        
def unique_prefixes(lst):
    root = TrieNode('*')
    add_list(root, lst)
    print(shortest_unique_prefixes(root))

unique_prefixes(["dog", "cat", "apple", "apricot", "fish"])
unique_prefixes(["zebra", "dog", "duck", "dove"])