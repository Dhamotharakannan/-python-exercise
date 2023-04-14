def rounding_upto_decimal_places(num):
    num=round(num,2)
    return num
def circle_calculation(r):
    r=float(r)
    area=3.14*r*r
    area=rounding_upto_decimal_places(area)

    circumference=2*3.14*r
    circumference=rounding_upto_decimal_places(circumference)

    diameter=2*r
    return area,circumference,diameter

if __name__=="__main__":

    r=input("the radius:")
a,c,d=circle_calculation(r)
print("circle area:", a, '\n', "circle circumference:", c, '\n', 'circle diameter:', d)