# Problem 31: Generalize the above implementation of csv parser to support any delimiter and comments.

import sys

def parse_csv(filename,p,q):
   return [x[:-1].split(p) for x in open(filename,'r').readlines() if x[0]!=q]
filename=sys.argv[1]

delimmiter= input("Enter delimiter:")
comment_ind= input("Enter comment indicator:")
print('parse_csv(',filename,',',delimmiter,',',comment_ind,')=',parse_csv(filename,delimmiter,comment_ind))