h="hello world and practice makes perfect and hello world again"
l=h.split(" ")
print(l)
j=[]
for i in l:
    k=l.count(i)
    print(k)
    if k>=1 and i not in j:

        j.append(i)
print(" ".join(j))