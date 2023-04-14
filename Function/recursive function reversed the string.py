def length(y):

    if y==0:
        letter=(s[0])
        return letter

    else:
        letter=s[y]+(length(y-1))
        return letter
s="dhamu"
l=len(s)
print(len(s))
k=len(s)-1
print(k)
print(s[k])
print(length(0))
print(length(k))
