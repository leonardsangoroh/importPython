# check height of a person
# if greater than 120, they can ride, else they cannot
# also check age & determine how much they should pay

print("Welcome to the Roalercoaster!")
height = int(input("What is your height in cm?"))

if height > 120:
    print("You can ride the roalercoaster!")
    age = int(input("What is your age? "))
    if age < 12:
        print("Please pay $5.00")
    elif age <= 18:
        print("Please pay $7.00")
    else:
        print("Please pay $12.00")
else:
    print("Sorry, you have to grow taller before you can ride")

# coding exercise
# check whether the number is odd or even


number = int(input("Which number do you want to check? "))

result = number%2

if result == 1:
    print("odd")

else:
    print("even")