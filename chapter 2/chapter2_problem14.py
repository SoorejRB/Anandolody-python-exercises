# unique(["python", "java", "Python", "Java"], key=lambda s: s.lower())
# ["python", "java"]

def uniq(li,key):
    l = []
    for i in li:
        if key (i) not in l:
            l.append(key(i))

    return(l)
print(uniq(["python", "java", "Python", "Java"], key=lambda s: s.lower()))      