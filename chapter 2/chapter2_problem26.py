# Problem 26: Python provides a built-in function filter(f, a) that returns items of the list a for which f(item) returns true. Provide an implementation for filter using list comprehensions.

def filter(d,a):
   return [x for x in a if d(x) is True]
def even(y):
   return y%2==0
l=[1,2,3,4,5,6]
print('real list',l)
print(filter(even,l))