import os

def clear_screen():
    # 'nt' refers to Windows
    if os.name == 'nt':
        _ = os.system('cls')
    # 'posix' refers to Linux, macOS, Unix, etc.
    else:
        _ = os.system('clear')

# CASE INSENSITIVE BUT SIMPLE
class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, key):
        curr = self.root
        for c in key.lower():
            index = ord(c) - ord('a')
            if curr.children[index] == None:
                curr.children[index] = TrieNode()
            curr = curr.children[index]
        curr.end_of_word = True

    def search(self, key):
        curr = self.root
        for c in key.lower():
            index = ord(c) - ord('a')
            if curr.children[index] == None:
                return False
            curr = curr.children[index]
        return curr.end_of_word
    
    def is_prefix(self, prefix):
        curr = self.root
        for c in prefix:
            index = ord(c) - ord('a')
            if curr.children[index] is None:
                return False
            curr = curr.children[index]
        return True

# Complex / flexible version

class CTrieNode:
    def __init__(self):
        self.children = {}
        self.end_of_word = False

class CTrie:
    def __init__(self):
        self.root = CTrieNode()
    
    def insert(self, key):
        curr = self.root
        for c in key:
            if c not in curr.children.keys():
                curr.children[c] = CTrieNode()
            curr = curr.children[c]

        curr.end_of_word = True

    def search(self, key):
        curr = self.root
        for c in key:
            if c not in curr.children.keys():
                return False
            curr = curr.children[c]

        return curr.end_of_word
    
    def is_prefix(self, key):
        curr = self.root
        for c in key:
            if c not in curr.children.keys():
                return False
            curr = curr.children[c]
        return not curr.children == {}
    
    def is_empty(self):
        if not self.root.children:
            return True
        return False
    
    def delete(self, key):
    
    def _delete(node, key, depth):
        if not node:
            return False

        

        


            
clear_screen()

# Tests

T = CTrie()
T.insert("cow")
print(T.search("cow"))
T.insert("POTATO")
T.insert("cower")
print(T.search("POTATO"))
print(T.search("potato"))
print(T.search("cowe"))
print(T.search("cower"))
print(T.is_prefix("c"))
print(T.is_prefix("cow"))
print(T.is_prefix("cowe"))
print(T.is_prefix("cower"))
T.delete("cower")
print(T.search("cower"))

# Tests for simple Trie

# T = Trie()
# T.insert("cow")
# print(T.search("cow"))
# T.insert("POTATO")
# T.insert("cower")
# print(T.search("POTATO"))
# print(T.search("potato"))
# print(T.search("cowe"))
# print(T.search("cower"))
# print(T.is_prefix("cower"))

#DELETE METHOD COPIED TO REFERENCE

# def delete(self, word):
#     def _delete(node, word, depth):
#         if not node:
#             return False

#         # Base Case: Reached the end of the word
#         if depth == len(word):
#             # If the word was actually there, unmark it
#             if node.is_end_of_word:
#                 node.is_end_of_word = False
            
#             # Return True if this node can now be deleted by its parent
#             return len(node.children) == 0

#         char = word[depth]
#         if char in node.children:
#             # Recursively move to the next character
#             should_delete_child = _delete(node.children[char], word, depth + 1)

#             if should_delete_child:
#                 # Physically remove the child from the dictionary
#                 del node.children[char]
                
#                 # We can delete this node too if it's not a word-end and has no other children
#                 return not node.is_end_of_word and len(node.children) == 0
        
#         return False

#     # Start deletion from the root
#     if not self.search(word):
#         raise KeyError(f"Key '{word}' not found")
#     _delete(self.root, word, 0)