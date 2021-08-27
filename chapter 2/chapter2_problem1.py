# a list contain another list as member
a = [1,2]
b = [3,5,6,a]
print(b)

# builtin range fn
x = range(1, 4)
print(x)
print(x[0])
print(x[1])
print(x[2])
print(len(x))

# + and * operators in list
a = [1,2,3]
b = [4,5,6]
print(a+b)
print(a*2)


# negative index
x = [1,2,3,4]
print(x[-1])
print(x[-2])

#list slicing
x = [1,2,3,4]
print(x[0:2])
print(x[0:-2])
print(x[:2])
print(x[2:])

x = [1,2,3,4,5,6,7,8,9]
print(x[0:6:2])
print(x[::-1]) #reverse list

#Presence of a key in a list can be tested using in operator
x = [1,2,3,4]
print(2 in x)
print(10 in x)

#append
x = [1,2,3,4]
x.append(100)
print(x)

#problem
x = [0, 1, [2]]
# x[2] = 3
x[2][0] = 3
print(x)

x[2].append(4)
print(x)

# x.append(22)
# print(x)

x[2] = 2
print(x)
