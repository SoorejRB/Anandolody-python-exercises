# unique([1, 2, 1, 3, 2, 5])
# [1, 2, 3, 5]


# def unique(li):
     
#     li2 = []
#     li_set = set(li)
  
#     unique_li = (list(li_set))
#     for i in unique_li:
#         li2.append(i) 
#     print(li2) 
 

# li = [1, 2, 1, 3, 2, 5]
# unique(li)


def uniq(li):

    l = []
    for i in li:
        if i not in l:
            l.append(i)

    return(l)
print(uniq([1, 2, 1, 3, 2, 5]))


