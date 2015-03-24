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
