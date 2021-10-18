# Write a program reverse.py to print lines of a file in reverse order.


def rev():
    file = open("/home/sooraj/Desktop/python3/python/Anandolody-python-exercises/chapter 2/problem_17.txt","r")
    read = file.readlines()
    r = reversed(read)

    for i in r:
       print(i.rstrip())

rev()


