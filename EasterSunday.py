# File: EasterSunday.py
# Student: Hengzhi Zhang
# UT EID: hz6984
# Course Name: CS303E
# Date: 9/6/2022
# Description of Program: Outputs the month and date of Easter Sunday from a user-input year

y = int(input("Enter year: "))

a = (y % 19)
b = y // 100
c = y % 100
d = b // 4
e = b % 4
g = (8 * b + 13) // 25
h = int((19 * a + b - d - g + 15) % 30)
j = int(c / 4)
k = c % 4
m = (a + 11 * h) // 319
r = (2 * e + 2 * j - k - h + m + 32) % 7
n = int((h - m + r + 90) // 25)
p = int((h - m + r + n + 19) % 32)
print("In " + str(y) + " Easter Sunday is on month " + str(n) + " and day " + str(p))
