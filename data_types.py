age = input("How old are you?")
age = int(age)

if age == 16:
    print("You can get your driver's!")
elif age == 15:
    print("You can get your learner's!")
elif age < 15:
    print("You are too young to drive.")
else:
    print("You probably already have your license.")