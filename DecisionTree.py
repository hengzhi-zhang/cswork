# File: DecisionTree.py
# Student: Hengzhi Zhang
# UT EID: hz6984
# Course Name: CS303E
# Date: 9/18/22
# Description of Program: This program asks a user for a person's age,
# income, if they're a student, and if they
# have good credit. It will then tell you if the person can purchase a computer.


age = int(input("Please enter person's age: "))

income = str(input("Person's income (Highs, Medium, Low): "))

isStudent = str(input("Is this person a student (Yes or No): "))

credit = str(input("Does this person have good credit (Yes or No): "))

accept = False

if age <= 30:

    if isStudent == "Yes":

        accept = True

    else:

        accept = False

else:

    if age <= 40:

            accept = True

    elif age >40:

        if isStudent:

            if credit == "No":

                accept = True

            else:

                accept = False

if accept:

    print("This person will purchase a computer")

else:

    print("This person will not purchase a computer")










