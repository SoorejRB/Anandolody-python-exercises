# import math

# print(math.factorial(4))

# print(math.factorial(10))

def fact(x):
    x+=1
    f =1
    for i in range (x):
        if i == 0:
            continue
        else:
            f = f * i
    
         
    print(f)

fact(4)

        