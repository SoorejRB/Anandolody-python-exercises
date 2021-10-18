# # Problem 20: Implement unix command grep. The grep command takes a string and a file as arguments and prints all lines in the file which contain the specified string.

import sys

filename=sys.argv[1]
f=open(filename,'r')
l=[]
l.extend(f.readlines())
j= input('Enter your string:')
for i in l:
   if j in i:
      print(i)