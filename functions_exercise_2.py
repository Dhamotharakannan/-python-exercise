def calculate_area (b,h,shape='triangle'):
    if shape=="triangle":
        tria_area=b*h/2
        print("triangle area:",tria_area)

    else:
        rectangle_area=h*b
        print("rectangle area:",rectangle_area)
#Calculate area of triangle whose base is 10 and height is 5
calculate_area(10,5,"triangle")
# Calculate area of a rectangle whose length is 20 and width is 30
calculate_area(20,30,"rect")