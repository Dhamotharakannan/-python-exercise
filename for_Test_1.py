my_call= "heads"
result = ["heads","tails","tails","heads","tails","heads","heads","tails","tails","tails"]
total=0
for i in result:
    if i==my_call:
        total = total + 1

print("total heads",total)