
def Find_Max_Zeroes(N,string):
    
    T = N*string
    count = 0
    str = ''

    for elem in T:
        if elem == '0':
            str+=elem
        else:
            if len(str) >= count:
                count = len(str)
            str = ''
    
    print(T)
    return count 
    
print(Find_Max_Zeroes(7,'010000011101'))

