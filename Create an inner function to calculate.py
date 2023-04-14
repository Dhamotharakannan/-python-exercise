#Exercise 5: Create an inner function to calculate the addition in the following way
#Create an outer function that will accept two parameters, a and b
#Create an inner function inside an outer function that will calculate the addition of a and b
#At last, an outer function will add 5 into addition and return it
def outer_addition(a,b):
    def inner_addition(a,b):
        return a+b
    return inner_addition(a,b)+5

print("Ex 1:",outer_addition(4,7))
print("Ex 2:",outer_addition(10,22))