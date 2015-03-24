# The sum of the squares of the first ten natural numbers is,
# 1^2 + 2^2 + ... + 10^2 = 385
# The square of the sum of the first ten natural numbers is,
# (1 + 2 + ... + 10)^2 = 55^2 = 3025
# 
# Find the difference$$ between the sum of the squares of the first one hundred natural numbers and the square of the sum.
#
# Judith Gammie
# 25th March 2015

def sumsquarediff(n):

    sumofsquares = 0
    long(sumofsquares)
    squareofsums = 0
    long(squareofsums)

    for i in range (1,n+1):
        sumofsquares += i*i
        squareofsums += i
    
    squareofsums = squareofsums*squareofsums
    print (squareofsums - sumofsquares)

sumsquarediff(100)
