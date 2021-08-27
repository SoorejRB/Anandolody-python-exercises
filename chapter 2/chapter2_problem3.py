# >>> sum(["hello", "world"])
# "helloworld"
# >>> sum(["aa", "bb", "cc"])
# "aabbcc"



# sum fn doesnt work with string

def sum(list):
    x = ""
    for i in list:
        x = x + i
    return x

print(sum(["mango", "apple", "orange"]))

