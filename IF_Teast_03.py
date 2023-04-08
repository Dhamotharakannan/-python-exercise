tamilnadu=["chennai","madurai","sivakasi"]
maharashtra=["mumbai","pune","thane"]
karnataka=["bengaluru","musuru","mangaluru"]
city_1=input("city_1:")
city_2=input("City_2:")
if city_1 in tamilnadu and city_2 in tamilnadu:
    print("Both cities in tanilnadu")
elif city_1 in maharashtra and city_2 in maharashtra:
    print("Both cities in maharashtra")
elif city_1 in karnataka and city_2 in karnataka:
    print("Both cities in karnadaga")
else:
    print("Both cities are not in same state")