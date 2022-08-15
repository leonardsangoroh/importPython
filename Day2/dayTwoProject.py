# create a tip calculator
# the amount should be in 2 decimal places

print("Welcome to the tip calculator")

total = input("What was the total bill? ")
totalInteger = int(total)

tipPercentage = input("What % would you like to give? 10, 12, or, 15?")
tipPercentageInteger = int(tipPercentage)

peopleCount = input("How many people to split the bill?")
peopleCountInteger = int(peopleCount)

amountPerPerson = round((totalInteger * (1 + (tipPercentageInteger/100))) / peopleCountInteger, 2)

print(f"Each person should pay: $ {amountPerPerson}")