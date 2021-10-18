# import os.path, time

# print("Last modified: %s" % time.ctime(os.path.getmtime("/home/sooraj/Desktop/python3/python/Anandolody-python-exercises/chapter 2/chapter3_problem1.py")))
# print("Created: %s" % time.ctime(os.path.getctime("/home/sooraj/Desktop/python3/python/Anandolody-python-exercises/chapter 2/chapter3_problem1.py")))



import os, time
def get_information(directory):
    file_list = []
    for i in os.listdir(directory):
        a = os.stat(os.path.join(directory,i))
        file_list.append([i,time.ctime(a.st_atime),time.ctime(a.st_ctime)])
    return file_list

data = get_information("/home/sooraj/Desktop/python3/python/Anandolody-python-exercises/chapter 2/chapter3_problem1.py")
print(data)
