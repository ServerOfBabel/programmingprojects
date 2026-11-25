#ifelselesson2

response = input("Would you like food? (Y/N): ")

if response == "Y":
    print("Have some food!")
else:
    print("No food for you!")

name = input("What is your Name?: ")

if name == "":
    print("you did not type in your name!")
else:
    print(f"Hello {name}!")

for_sale = True

if for_sale:
    print("This item is for sale!")
else:
    print("This item is not for sale!")

online = bool(input("Is this person online? (True/False)"))

if online:
    print("The user is online!")
else:
    print("The user is offline :( ")