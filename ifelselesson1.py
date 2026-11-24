#if else lessons

age = int(input("Enter your age: "))

if age >= 100:
    print("You are older than biden!!")
elif age >= 18:
    print("You are now signed up to vote!")
elif age < 0:
    print("You haven't been born yet to vote!!")
else:
    print("You cant vote for biden!")