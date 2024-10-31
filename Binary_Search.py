from math import floor

def Binary_Search(array,elem):
    start = 0
    end = len(array) -1 
    middle = floor((start + end)/2)
    
    while not(array[middle] == elem):
        if array[middle] < elem:
            end = middle -1
        else:
            start  = middle + 1
        middle = floor((start + end) /2)

    if array[middle] == elem:
        return middle

    return middle
    
print(Binary_Search([1,3,4,13,26,39,41,54],13))
    


