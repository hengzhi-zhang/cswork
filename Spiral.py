#  File: Spiral.py
#  Student Name: Hengzhi Zhang
#  Student UT EID: hz6984
#  Partner Name: Ethan Mason
#  Partner UT EID: em45486
#  Course Name: CS 313E
#  TA Name: Rahaf

import sys
# Input: n is an odd integer between 1 and 100
# Output: returns a 2-D list representing a spiral
# This function creates a spiral of size n
def create_spiral(n):

    oneList = [1]
    if n == 1 :
        return oneList
    x = n//2
    y = n//2
    flag = False
    index = 1
    step = 1
    numSpirals = (n//2)+1
    bigList = []
    for r in range(n):
        smallList = []
        for c in range(n):
            smallList.append(0)
        bigList.append(smallList)

    bigList[x][y] = index
    direction = 0
    for i in range(numSpirals*4-3):
        temp = 0
        while temp < step:
            if direction == 0:
                index+=1
                y+=1
                bigList[x][y] = index


            if direction == 1:
                index+=1
                x+=1
                bigList[x][y] = index


            if direction == 2:
                index+=1
                y-= 1
                bigList[x][y] = index


            if direction == 3:
                index+=1
                x-=1
                bigList[x][y] = index

            temp += 1

        if direction == 3:
            direction = 0
        else:
            direction +=1

        if flag:
            if step == n-1:
                pass
            else:
                step+=1
                flag = not flag
        else:
            flag = not flag

    return bigList

    
# Input: spiral is a 2-D list and n is an integer
# Output: returns an integer that is the sum of the
#         numbers adjacent to n in the spiral
#         if n is not in the grid return 0
def sum_adjacent_numbers(spiral, n):

    sum = 0
    indx = 0
    indy = 0
    for x in range(len(spiral)):
        for y in range(len(spiral)):
            if spiral[x][y]==n:
                indx = x
                indy = y

    try:
        if indx != 0:
           sum+= spiral[indx-1][indy]
    except:
        pass
    try:
        if indx != 0:
           sum+= spiral[indx-1][indy+1]
    except:
        pass
    try:
           sum+= spiral[indx][indy+1]
    except:
        pass
    try:
           sum+= spiral[indx+1][indy+1]
    except:
        pass
    try:
           sum+= spiral[indx+1][indy]
    except:
        pass
    try:
        if indy != 0:
           sum+= spiral[indx+1][indy-1]
    except:
        pass
    try:
        if indy != 0:
           sum+= spiral[indx][indy-1]
    except:
        pass
    try:
        if indx != 0 and indy != 0:
           sum+= spiral[indx-1][indy-1]
    except:
        pass

    return sum
    print("")

def main():

    debug = True
    if debug:
        in_file = open('spiral.in')
    else:
        in_file = sys.stdin

    try:
        # read the spiral dimension, add one if needed
        line = int(in_file.readline())
        if(line % 2) == 0:
            line+=1
    except:
        exit()



    # create the spiral of size line
    spir = create_spiral(line)
    for x in spir:
        print(x)
    # for each additional number in input
    num = 0
    for l in in_file:
        # read the number, catch and handle exception
        try:
            num = int(l)
        except:
            # if an exception happened, end the program
            exit()

        # add the adjacent numbers
        output = sum_adjacent_numbers(spir, num)
        # print the result
        print(str(output))



if __name__ == "__main__":
    main()