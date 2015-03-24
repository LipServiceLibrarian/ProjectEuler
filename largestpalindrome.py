#A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

#Find the largest palindrome made from the product of two 3-digit numbers.
#
# Judith Gammie
# 25th March 2015


def largestpalindrome():
 a = []
 b = []

 for i in range (900,999):
     a.append(i)
 b = a

 for val in reversed(a):
     for secondval in reversed(b):
         if ispalindrome(val*secondval):
               print val*secondval
               return
 
def ispalindrome(n):
   if str(n) == str(n)[::-1]: 
       return True
   else:
       return False

largestpalindrome()
