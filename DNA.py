#  File: DNA.py
#  Student Name: Hengzhi Zhang and Ethan Mason
#  Student UT EID: hz6984 and em45486
#  Course Name: CS 313E
#  TA Name: 

# Input: s1 and s2 are two strings that represent strands of DNA
# Output: returns a sorted list of substrings that are the longest 
#         common subsequence. The list is empty if there are no 
#         common subsequences.

# returns a list with the longest subsequences of s1 and s2
def longest_subsequence (s1, s2):
    biggest = ""
    answerList = []
    possibleList = []
    # this loop goes through the length of the first string
    for x in range(len(s1)):
        string1 = s1[x:]
        #
        for x in range(len(string1)):
            sub = string1[:x]
            if sub in s2:
                if sub > biggest:
                    biggest = sub
                else:
                    possibleList.append(sub)
    answerList.append(biggest)

    for word in possibleList:
        if len(word) == len(biggest):
            answerList.append(word)
    return answerList
    # ADD CODE HERE

def main():
    # ADD CODE HERE, using comments as a guide
  
    # read the data
    file1 = open("DNA.in", 'r')
    numPairs = int(file1.readline())
    # for each pair
    for x in range(numPairs):
        # call longest_subsequence
        pair1 = file1.readline()
        pair2 = file1.readline()
        long = longest_subsequence(pair1, pair2)

        # write out result(s)
        if long[0] != "":
            for subsequence in long:
                print(subsequence)
        else:
            print("No Common Sequence Found")


        # insert blank line
        print("")

if __name__ == "__main__":
  main()
