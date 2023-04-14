#Write a program to create a function show_employee() using the following conditions.

#It should accept the employee’s name and salary and display both.
#If the salary is missing in the function call then assign default value 9000 to salary
def employee(a,b=9000):
    print(f"employee name:{a} and salary:{b}")
employee("dhamu",15000)
employee("kannna")