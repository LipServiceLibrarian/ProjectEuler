def findtheprime():

    primecount = 0
    for i in range (3, 10000000):
        if is_prime(i):
            primecount += 1
        if primecount == 10001:
                print i
                break

def is_prime(n):
   for i in range (2, n/2):
       if (n % i) == 0:
           return False
   return True

findtheprime()
