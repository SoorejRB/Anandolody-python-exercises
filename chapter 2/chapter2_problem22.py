# Problem 22: The above wrap program is not so nice because it is breaking the line at middle of any word. Can you write a new program wordwrap.py that works like wrap.py, but breaks the line only at the word boundaries?

# import sys
# def wrap(x,l):
#     i=0
#     k=0
#     s=len(open(x).read().split())
#     q=['']*s
#     f=open(x).read().split()
#     w=0
#     while(i<s):
#         if(len(f[i])<=(l-len(q[w]))):
#           q[w]=q[w]+' '+f[i]
#           i=i+1
#         else:
#           q[w]=q[w]+'\n'
#           w=w+1
#     i=1
#     while(i<len(q)):
#         q[0]=q[0]+q[i]
#         i=i+1
#     return q[0]
# print(wrap(sys.argv[1],int(sys.argv[2])))

import sys
filename=sys.argv[1]
c=int(sys.argv[2])
f=open(filename,'r')
l=[]
l.extend(f.readlines())
for i in l:
   new=i
   while len(new)>c :
      if new[c-1]!=' ':
         for j in range(c-1):
            if new[:c-1][-j]==' ':
               print(new[:c-1+(-j)])
               break;
         new=new[c-1+(-j):]
      else:
         print(new[:c-1])
         new=new[c-1:]
   print(new[:-1])