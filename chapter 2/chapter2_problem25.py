# Problem 25: Python provides a built-in function map that applies a function to each element of a list. Provide an implementation for map using list comprehensions.                                                                                                                                                                                                     
def square(x):
    return x*x
def cube(x):
    return x**3
def map1(y,x):
    return [y(a) for a in x]
print(map1(chr,range(97,123)))