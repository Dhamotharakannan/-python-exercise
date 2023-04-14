j=[]
for k in range(2000,2200):
    i=str(k)
    if ((int(i[0])%2==0) and (int(i[1])%2==0) and (int(i[2])%2==0) and (int(i[3])%2==0)):
        j.append(i)
print(",".join(j))