# Write a function to compute the number of python files (.py extension) in a specified directory recursively.

import os
import sys

def counts(files):
    return [file for file in files if '.py' in file]

files=os.listdir(sys.argv[1])
pyfiles=counts(files)

print(len(pyfiles))