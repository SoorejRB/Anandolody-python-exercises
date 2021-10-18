# Problem 28: Write a function enumerate that takes a list and returns a list of tuples containing (index,item) for each item in the list.

l=[]
def enumerate(list):
  for i in list:
    l.append(list.index(i))
  print(zip(l,list))
enumerate(['b','c','d','f'])