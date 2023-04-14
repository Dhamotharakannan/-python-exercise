#Write a password generator in Python. Be creative with how you generate passwords - strong passwords have a mix of
# lowercase letters, uppercase letters, numbers, and symbols. The passwords should be random, generating a new password
# every time the user asks for a new password. Include your run-time code in a main method.
#new_password=input("My New Password:")
import string

for i in string.ascii_lowercase:
    print(i,end= "")
for j in string.ascii_uppercase:
    print(j,end= "")
num=[1234567890]
num=str(num)
for n in num:
    print(n,end="")
sym=['']
print(sym)