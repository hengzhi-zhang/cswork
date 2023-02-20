# File: FindPrimeFactors.py
# Student: Hengzhi Zhang
# UT EID: hz6984
# Course Name: CS303E
#
# Date: 10/19/22
# Description of Program: This program finds the prime factorization of a given user-input number!
import math
def isPrime ( num ):
    """ Test whether num is prime . """
    # Deal with evens and numbers < 2.
    if ( num < 2 or num % 2 == 0 ):
        return ( num == 2 )
    # See if there are any odd divisors
    # up to the square root of num.
    divisor = 3
    while ( divisor <= math.sqrt( num )):
        if ( num % divisor == 0 ) :
            return False
        else :
            divisor += 2
    return True

def findNextPrime ( num ):
    """ Find the first prime > num. """
    if ( num < 2 ) :
        return 2
    # If (num >= 2 and num is even ), the
    # next prime after num is at least
    # (num - 1) + 2 , which is odd.
    if ( num % 2 == 0) :
        num -= 1
    guess = num + 2

    while ( not isPrime ( guess )):
        guess += 2
    return guess

print("Find Prime Factors: ")
while 1:
    answer = []
    num = int(input("Enter a positive integer (or 0 to stop): "))
    store = num
    if num == 0:
        print("Goodbye!")
        break
    if num == 1:
        print("1 has no prime factorization. ")
        continue
    if num <0:
        print("Negative integer entered. Try again.")
        continue
    while not answer:
        if isPrime(num):
            answer = [num]

# need to work on this else statement and then im done
        else:
            my_list = []
            d = 2
            while num >1:
                if num % d == 0:
                    my_list.append(d)
                    num = num / d
                else:
                    d = findNextPrime(d)
            answer = my_list

    print("The prime factorization of " + str(store) + " is " + str(answer))
    print("")



