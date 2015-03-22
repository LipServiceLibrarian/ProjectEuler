# Project Euler - Problem 1 
# 'Multiples of 3 and 5'
#
# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.

# Judith Gammie
# 23rd March 2015
# correct answer confirmed on ProjectEuler

def multiplesof3and5():
    summation = 0
    long(summation)
    for number in range(0,1000):
        if number%3 == 0 or number%5 == 0:
            summation += number
    return summation

print multiplesof3and5()
