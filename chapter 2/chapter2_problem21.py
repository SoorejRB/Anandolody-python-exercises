# Problem 21: Write a program wrap.py that takes filename and width as aruguments and wraps the lines longer than width.
import sys

def wrap(filename):
  k = int(sys.argv[2])
  f=open(filename).readlines()
  for i in f:
    x=i
    while len(x)>k:
      print(x[:k])
      x=x[k:]
      print(x)
wrap(sys.argv[1])