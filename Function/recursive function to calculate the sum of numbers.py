#Write a program to create a recursive function to calculate the sum of numbers from 0 to 10.
def the_sum_of_numbers(n):
    if n==0:
        total = 0
        return total
    else:
        total = n + the_sum_of_numbers(n - 1)
        return total


print("Ex 1:the_sum_of_numbers is",the_sum_of_numbers(10))
print("Ex 2:the_sum_of_numbers is",the_sum_of_numbers(12))
print("Ex 3:the_sum_of_numbers is",the_sum_of_numbers(0))
print("Ex 4:the_sum_of_numbers is",the_sum_of_numbers(00))