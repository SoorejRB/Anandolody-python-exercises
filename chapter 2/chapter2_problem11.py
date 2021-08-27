# dups([1, 2, 1, 3, 2, 5])
# [1, 2]

def uniq(li):

    l = []
    k = []
    for i in li:
        if i not in l:
            l.append(i)
        else:
            k.append(i)

    return k
   
print(uniq([1, 2, 1, 3, 2, 5]))


    
    
