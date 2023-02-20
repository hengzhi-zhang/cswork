# CS 303E Quiz 4C
# do NOT rename this file, otherwise Gradescope will not accept your submission
# also, do NOT change any of the function names or parameters

# Problem 1: Large Elements
import math
def largeElements(lst):

    newList = []
    for x in range(len(lst)):
        if x!= len(lst)-1 and lst[x] > lst[x+1]:
            newList.append(lst[x])
    return newList


# Problem 1: Unequal Midterms
def computeCourseGrade(m1, m2, m3):
    if m1 >= m2 and m1 >= m3:
        return math.floor((.4*m1) + (.3*m2) + (.3*m3))

    if m2 >= m1 and m2 >= m3:
        return math.floor((.4 * m2) + (.3 * m1) + (.3 * m3))

    if m3 >= m1 and m3 >= m2:
        return math.floor((.4 * m3) + (.3 * m1) + (.3 * m2))

def getStudentGrades(lst):

    newerList = []
    for x in lst:
        newerList.append([x[0],computeCourseGrade(x[1],x[2],x[3])])
    return newerList


if __name__ == '__main__':


     print(largeElements([6, -1, 28, 27, -6, 29, -1, -21, -20, -28, 13, 15, 2]))
     print(largeElements([5, 4, 3, 2, 1, 0]))
     print(largeElements([1, 2, 4, 8, 16, 32]))


     print(computeCourseGrade(85, 79, 85))
     print(computeCourseGrade(85, 92, 83))
     print(getStudentGrades([["Hannah", 85, 79, 85], ["Eli", 85, 92, 83], ["Elena", 96, 95, 100]]))

pass
