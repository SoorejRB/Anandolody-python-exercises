# Problem 35: Write a program to count frequency of characters in a given file. Can you use character frequency to tell whether the given file is a Python program file, C program file or a text file?

import sys
def freq(x):
 dic = {}
 for i in x:
  dic[i] = dic.get(i,0) + 1
 return dic

a=input("enter your string")
print(freq(a))