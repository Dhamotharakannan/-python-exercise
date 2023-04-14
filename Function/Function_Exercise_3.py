
def addition(a, b):
    total = a + b
    print("This is addition:", total)
    return total

def subraction(a, b):
    sub = a - b
    print("This is subraction:", sub)
    return sub

def multiplication(a, b):
    multi = a * b
    print("This is multiplication:", multi)
    return multi
def calculation (a,b,type="add"):

    if  type=="add":
        addition(a,b)
    elif type=="sub":
        subraction(a,b)
    elif type=="multi":
        multiplication(a,b)

    else:
        print(("i dint know calculation type"))

Problem_1 =calculation(5,3,"add")
Problem_2 =calculation(6,33)
Problem_3 =calculation(55,10,"sub")
Problem_4 =calculation(10,44,"multi")
Problem_5 =calculation(33,21,"aaa")

addition(5,22)
subraction(44,20)
multiplication(33,4)