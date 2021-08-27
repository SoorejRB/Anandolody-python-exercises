# print(cumulative_product([1, 2, 3, 4]))

lista = [1, 2, 3, 4, 5]
cumu_list = []
a = 1

for i in range(0, len(lista)):
     a*=lista[i]
     cumu_list.append(a)

print(cumu_list)
