# Project Euler - Problem 5 'Smallest Multiple'
#
# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

#What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
#
# Judith Gammie
# 23rd March 2015

def smallestmultiple():
   number = 20
   long(number)
   flag = 'false'
   while (flag == 'false'):
       innerflag = 'true';
       for i in range (11,20):
           if (number % i != 0):
               innerflag = 'false'
       if innerflag == 'true':
           break
       number += 20
   return number

print smallestmultiple()
