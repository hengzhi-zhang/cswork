#  File: BST_Cipher.py
#  Description: BST implementation of phrase substitution cipher
#  Student Name: Hengzhi Zhang
#  Student UT EID: hz6984
#  Partner Name: Ethan Mason
#  Partner UT EID: em45486

import sys

# One node in the BST Cipher Tree
class Node:
    def __init__(self, ch):
        self.ch = ch
        self.left = None
        self.right = None

# Attributes and methods for the BST Tree
class Tree:

    # Create the BST Cipher tree based on the key
    def __init__(self, key):

        # ADD CODE
        self.root = None
        self.makeTree(key)


    # Helper method to make the tree
    def makeTree(self,key):
        key = self.clean_string(key)
        for i in range(len(key)):
            self.insert(key[i])


    # Insert one new charater to the BST Cipher tree
    def insert(self, ch):

        # ADD CODE
        self.root = self._insert_helper(self.root, ch)

    # Helper method to insert each character
    def _insert_helper(self, node, key):
        if self.isValidCh(key):
            if node is None:
                return Node(key)
            if key < node.ch:
                node.left = self._insert_helper(node.left, key)
            elif key > node.ch:
                node.right = self._insert_helper(node.right, key)
            return node

    # Encrypts a text message using the BST Tree
    def encrypt(self, message):

        # ADD CODE
        encrypted = ''
        for i in range(len(message)):
            character = message[i]
            if self.isValidCh(character):
                encrypted += self.encrypt_ch(character) + "!"

        return encrypted[:-1]

    # Encrypts a single character
    def encrypt_ch(self, ch):

            return self.encrypt_ch_helper(self.root,ch)

    # Helper method for the encrypt_ch method
    def encrypt_ch_helper(self,node, ch):

        # ADD CODE
        if node is not None and ch == node.ch and ch == self.root.ch :
            return "*"

        elif node is not None and ch == node.ch:
            return ""

        elif node.left is not None and ch < node.ch:
            return "<" + self.encrypt_ch_helper(node.left,ch)

        elif node.right is not None:
            return ">" + self.encrypt_ch_helper(node.right,ch)

        else:
            return ""

    # Decrypts an encrypted message using the same BST Tree
    def decrypt(self, codes_string):

        # ADD CODE
        decrypted = ''
        codes_string_list = codes_string.split("!")
        for code in codes_string_list:
            if len(code) < self.height():
                decrypted += self.decrypt_code(code)

        return decrypted




    # Decrypts a single code
    def decrypt_code(self, code):

        # ADD CODE
        current = self.root
        for i in range(len(code)):
            if code[i] == "<":
                current = current.left

            elif code[i] == ">":
                current = current.right

            else:
                return self.root.ch
        return current.ch


    # Get printed version of BST for debugging
    def BST_print(self):
        if self.root is None:
            return
        self.BST_print_helper(self.root)

    # Prints a BST subtree
    def BST_print_helper(self, node, level=0):
        if node is not None:
            if node.right is not None:
                self.BST_print_helper(node.right, level + 1)
            print('     ' * level + '->', node.ch)
            if node.left is not None:
                self.BST_print_helper(node.left, level + 1)

    # Utility method
    def isValidLetter(self, ch):
        if (ch >= "a" and ch <= "z"):
            return True
        return False

    # Utility method
    def isValidCh(self, ch):
        if (ch == " " or self.isValidLetter(ch)):
            return True
        return False

    def height(self):
        return self._height(self.root)

    def _height(self, node):
        if node is None:
            return 0
        left_height = self._height(node.left)
        right_height = self._height(node.right)
        return max(left_height, right_height) + 1

    # Scrubs string for lowercase and valid characters
    def clean_string(self,s):
        cleaned = ''
        s = s.lower()
        for char in s:
            if self.isValidCh(char):
                cleaned += char

        return cleaned

# =============================================================================
#                    NEW DRIVER CODE
# =============================================================================


def main():

    # Debug flag - set to False before submitting
    debug = False
    if debug:
        in_data = open('bst_cipher.in')
    else:
        in_data = sys.stdin

    # read encryption key
    key = in_data.readline().strip()

    # create a Tree object
    key_tree = Tree(key)


    #key_tree.BST_print()

    # read string to be encrypted
    text_message = in_data.readline().strip()

    # print the encryption
    print(key_tree.encrypt(text_message))

    # read the string to be decrypted
    coded_message = in_data.readline().strip()

    # print the decryption
    print(key_tree.decrypt(coded_message))


if __name__ == "__main__":
    main()
