# File: WordleAssistant.py
# Student: Hengzhi Zhang
# UT EID: hz6984
# Course Name: CS303E
#
# Date: 11/02/2022
# Description of Program: This program defines functions to help a user guess the correct wordle word.
# A user can get a list of words that matches words which include certain letters, doesn't contain certain letters, or has certain letters in certain positions.
def createWordlist(filename):
    """ Read words from the provided file and store them in a list.
    The file contains only lowercase ascii characters, are sorted
    alphabetically, one word per line. Filter out any words that are
    not 5 letters long, have duplicate letters, or end in 's'. Return
    the list of words and the number of words as a pair. """
    ...
    myList = []
    count = 0
    newFile = open(filename, "r")
    word = newFile.readline().strip()
    while word:
        if word[len(word)-1] != "s" and len(word) == 5 and len(set(word)) == len(word) :
            count += 1
            myList.append(word)
        word = newFile.readline().strip()
    return myList, count

def containsAll(wordlist, include):
    """ Given your wordlist, return a set of all words from the wordlist
    that contain all of the letters in the string include.
    """
    ...
    newSet = set()
    for word in wordlist:
        count = 0
        for character in include:
            #only matters if the last character is true
            if character in word:
                count += 1
        if count == len(include):
            newSet.add(word)

    return newSet


def containsNone(wordlist, exclude):
    """ Given your wordlist, return a set of all words from the wordlist
    that do not contain any of the letters in the string exclude.
    """
    ...
    newSet = set()
    for word in wordlist:
       count = 0
       for character in exclude:
           #only matters if the last character is true
           if character not in word:
               count += 1
       if count == len(exclude):
           newSet.add(word)

    return newSet


def containsAtPositions(wordlist, posInfo):
    """ posInfo is a dictionary that maps letters to positions.
    You can assume that the positions are in [0..4]. Return a set of
    all words from the wordlist that contain the letters from the
    dictionary at the indicated positions. For example, given posInfo
    {'a': 0, 'y': 4}.  This function might return the set:
    {'angry', 'aptly', 'amply', 'amity', 'artsy', 'agony'}. """
    ...
    newSet = set()
    keys = list(posInfo.keys())
    values = list(posInfo.values())

    for word in wordlist:
        count = 0
        for x in range(len(keys)):
            if keys[x] == word[values[x]]:
                count += 1
        if count == len(keys):
            newSet.add(word)

    return newSet




def getPossibleWords(wordlist, posInfo, include, exclude):
    """ Finally, given a wordlist, dictionary posInfo, and
    strings include and exclude, return the set of all words from
    the wordlist that contains the words that satisfy all of
    the following:
    * has letters in positions indicated in posInfo
    * contains all letters from string include
    * contains none of the letters from string exclude.
    """
    ...
    newSet = set()
    for word in wordlist:
        if word in containsAtPositions(wordlist, posInfo) and word in containsAll(wordlist, include) \
                and word in containsNone(wordlist, exclude):
            newSet.add(word)
    return newSet



