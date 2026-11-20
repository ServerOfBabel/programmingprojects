#exercise 1 rectangle area calc & shopping cart programs

length = float(input("Enter the length: "))
width = float(input("Enter the width: "))
area = length * width

item = input("What item would you like to buy?: ")
price = float(input("What is the price?: "))
quantity = int(input("How many would you like?: "))
total = price * quantity



print(f"The area is: {area}cm")
print(f"you have bought {quantity} x {item}/s for {total}")
