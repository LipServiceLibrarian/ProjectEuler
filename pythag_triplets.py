import math
def pythag_triplets():
    for i in range (1,1000):
        for j in range (i,1000):
            k_squared = (i*i) + (j*j)
            if (is_square(k_squared) and i + j + math.sqrt(k_squared) == 1000):
                print i * j * math.sqrt(k_squared)
                break

def is_square(number):
    root = math.sqrt(number)
    if int(root + 0.5) ** 2 == number:
        return True
    else:
        return False

pythag_triplets()
