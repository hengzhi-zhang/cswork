# File: Student.py
# Student: Hengzhi Zhang
# UT EID: hz6984
# Course Name: CS303E
#
# Date: 10/8/22
# Description of Program: This is the definiton of the Student class which has various methods
# related to exam grades

class Student:

    def __init__(self, name = None, exam1 = None, exam2 = None):
        self.__name = name
        self.__exam1 = exam1
        self.__exam2 = exam2


    def __str__(self):

        return "Student: " + str(self.__name) + "\r\n" + "Exam1: " + \
               str(self.__exam1) + "\r\n" + "Exam2: " + str(self.__exam2)

    def getName(self):
        return self.__name

    def getAverage(self):
        if self.__exam1==None or self.__exam2==None:
            print("Some exam grades not available")
        else:
            return (self.__exam2+self.__exam1)/2


    def getExam1Grade(self):
        return self.__exam1
    def getExam2Grade(self):
        return self.__exam2
    def setExam1Grade(self, grade):
        self.__exam1 = grade
    def setExam2Grade(self, grade2):
        self.__exam2 = grade2
