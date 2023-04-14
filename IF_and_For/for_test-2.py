for i in range(1,6):
    print(f"You ran {i} km")
    tired = input("yes/on:")
    if tired == 'yes':
        break

if i == 5:
    print("You finished 5 km")
else:
    print("You not finished the race")