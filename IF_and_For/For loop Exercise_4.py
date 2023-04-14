#Write a program that prints following shape
def print_pattern(a=5):
    for k in range(0,a):
        n = ""
        for l in range(k):
           n=n+"*"
        print(n)
print_pattern(7)
