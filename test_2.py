#list
numbers=[22,32,44,48,54]
#1.find maximum
print("1.The Maximum Value: ",max(numbers))
#2.reverse the order
numbers.reverse()
print("2.Reverse the order",numbers)
#3.Add 66 at the end of this list
numbers.append(66)
print("3.Add 66 at the end of this list",numbers)
#4.Add 40 next to 48
numbers.insert(2,40)
print("4.Add 40 next to 48:",numbers)
#5.length
print("5.Total length of the list",len(numbers))
#6.total
print("6.Total:",sum(numbers))
#7.Add first 3 number
print("7.Add first 3 values:",sum(numbers[0:3]))
#8.Replace 40 to 50
numbers[2]=50
print("8.Replace 40 to 50:",numbers)
#9.Remove 50
numbers.remove(50)
print("9.Remove 50 :",numbers)
