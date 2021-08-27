# >>> group([1, 2, 3, 4, 5, 6, 7, 8, 9], 3)
# [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# >>> group([1, 2, 3, 4, 5, 6, 7, 8, 9], 4)
# [[1, 2, 3, 4], [5, 6, 7, 8], [9]]


# no output
def group(list,size):
    l = []
    y = len(list)
    for i in range(size):
       
        x = list[i]
        l.append(x)
        
    return l
print(group([1, 2, 3, 4, 5, 6, 7, 8, 9],3))

