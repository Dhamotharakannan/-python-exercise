tamilnadu=["chennai","madurai","sivakasi"]
maharashtra=["mumbai","pune","thane"]
karnataka=["bengaluru","musuru","mangaluru"]
city=input("city name:")
if city in tamilnadu:
    print("it is tamilnadu")
elif city in maharashtra:
    print("it is maharashtra")
elif city in karnataka:
    print("it is karnataka")
else:
    print("i dont know")