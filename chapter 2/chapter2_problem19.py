
# Problem 19: Implement unix commands head and tail. The head and tail commands take a file as argument and prints its first and last 10 lines of the file respectively.


import sys


def head(l):
   if len(l)>10:
      for i in range(10):
         print(l[i])
   else:
      for i in range(len(l)):
         print(l[i])


def tail(l):
    if len(l)>10:
       for i in range(len(l)-10,len(l)):
          print(l[i])
    else:
       for i in range(len(l)):
          print(l[i])
          
filename=sys.argv[1]
f=open("/home/sooraj/Desktop/python3/python/Anandolody-python-exercises/chapter 2/problem_19.txt",'r')
l=[]
l.extend(f.readlines())
print('____Head_____')
head(l)
print('_____Tail____')
tail(l)




