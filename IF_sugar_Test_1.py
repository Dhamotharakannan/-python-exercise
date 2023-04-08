sugar=input("Sugar Level:")
sugar=int(sugar)
if sugar >= 80 and sugar <=100:
    print("sugar level is normal")
elif sugar < 80:
    print("Low sugar")
else:
    print("high sugar")