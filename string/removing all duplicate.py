from collections import Counter
s="hello world and practice makes perfect and hello world again"
s=s.split(" ")
print(s)
j = Counter(s)
print(j)
r = " ".join(j.keys())
print(r)