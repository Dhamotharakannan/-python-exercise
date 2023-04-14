h="dhamu,vkp,the,good,bad"
n=h.split(",")
print(n)
f=sorted(n)
print(f)
k=h.join("-")
print(k)
print ( "-".join(f))

myDict = {"name": "John", "country": "Norway"}
mySeparator = "TEST"

x = mySeparator.join(myDict)

print(x)