# Using names.txt, begin by sorting it into alphabetical order. Then working out the 
# alphabetical value for each name, multiply this value by its alphabetical position 
# in the list to obtain a name score. For example, when the list is sorted into 
# alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th 
# name in the list. So, COLIN would obtain a score of 938 x 53 = 49714.
#
# What is the total of all the name scores in the file?
# 
# Judith Gammie
# 2 July 2015

def names_score(input_filename):
    with open(input_filename, 'r') as infile, open(r'temp.txt', 'w') as outfile:
        data = infile.read().replace('"','')
        outfile.write(data)

    list = open('temp.txt', 'r').read().split(',')
    list.sort()

    total_score = 0
    for item in list:
        sum = 0
        for c in item:
            sum = sum + (ord(c) - 64) 
        total = sum * (list.index(item) + 1)
        total_score = total_score + total
    return total_score

input = 'names.txt'
print names_score(input)
