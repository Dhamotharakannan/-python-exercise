d="0100,0011,1010,1001,1111"
l=d.split(",")
k=[]
for i in l:
    if not (int(i,2))%5:
        k.append(i)
print(",".join(k))
