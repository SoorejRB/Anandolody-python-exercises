# Write a program that takes one or more filenames as arguments and prints all the lines which are longer than 40 characters.

import sys

files=[]
for i in range(1,len(sys.argv)):
  files.append(sys.argv[i])	


def generate(files):
  for f in files:
    for line in open(f):
      if len(line)>40:
        print(line)

generate(files)