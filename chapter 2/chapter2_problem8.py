# cumulative sum of a list

# import math
# x = [1,2,3,4,5]

# print(math.cumulative_sum(x))    not working

lista = [1, 2, 3, 4, 5]
cumu_list = []
a = 0

for i in range(0, len(lista)):
     a+=lista[i]
     cumu_list.append(a)

print(cumu_list)
