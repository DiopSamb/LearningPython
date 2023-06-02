# Write a function named capital_indexes. 
# The function takes a single parameter, which is a string. 
# Your function should return a list of all the indexes in 
# the string that have capital letters.
# For example, calling capital_indexes("HeLlO") should return the list [0, 2, 4].


def capital_indexes(a):
    long = len(a)
    list = []
    for x in range(long):
        if a[x].isupper() is True :
            
            list.append(x)
    return list 
print(capital_indexes("HeLlO"))





