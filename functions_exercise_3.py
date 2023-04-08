def mathe_calculation(a,b,type="add"):
    if type=="add":
        addition=a+b
        print("Result",type,addition)
    elif type=="sub":
        if a>=b:
            subraction=a-b
        else:
         subraction=b-a
        print("Result",type,subraction)

    elif type=="multi":
        multiplication=a*b
        print("Result",type,multiplication)

    else:
        print("i dint know calculation type")
mathe_calculation(4,5,"add")
mathe_calculation(8,3,"sub")
mathe_calculation(2,9,"sub")
mathe_calculation(10,3,"multi")
mathe_calculation(4,6)
mathe_calculation(3,5,"aaa")