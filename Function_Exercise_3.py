def addition(a, b):
    total = a + b
    print("This is addition:", total)
def subraction(a, b):
    sub = a - b
    print("This is subraction:", sub)
def multiplication(a, b):
    multi = a * b
    print("This is multiplication:", multi)
def calculation (a,b,type="add"):
    if  type=="add":
        addition(a,b)
    elif type=="sub":
        subraction(a,b)
    elif type=="multi":
        multiplication(a,b)

    else:
        print(("i dint know calculation type"))

calculation(5,3,"add")
calculation(6,33)
calculation(55,10,"sub")
calculation(10,44,"multi")
calculation(33,21,"aaa")
addition(5,22)
subraction(44,20)
multiplication(33,4)