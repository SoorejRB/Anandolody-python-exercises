# Write a program  to count number of files for each extension in the given directory. The program should take a directory name as argument and print count and extension for each available file extension.


import os
import collections
extensions = collections.defaultdict(int)

for path, dirs, files in os.walk('/home/sooraj/Desktop/python3/python/Anandolody-python-exercises/chapter 2'):
   for filename in files:
       extensions[os.path.splitext(filename)[1].lower()] += 1

for key,value in extensions.items():
    print ('Extension: ', key, ' ', value, ' items')