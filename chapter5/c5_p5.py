#  Write a function to compute the total number of lines of code in all python files in the specified directory recursively.

import sys
import os

def pyfiles(dir):
  files=os.listdir(dir)
  for f in files:
    if '.py' in f:
      print(f,len(open(f).readlines()))

pyfiles(sys.argv[1])