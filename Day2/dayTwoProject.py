# create a tip calculator
# the amount should be in 2 decimal places

print("Welcome to the tip calculator")

total = input("What was the total bill? ")
totalInteger = int(total)

tipPercentage = input("What % would you like to give? 10, 12, or, 15?")
tipPercentageInteger = int(tipPercentage)

peopleCount = input("How many people to split the bill?")
peopleCountInteger = int(peopleCount)

#round does not set the result to specified number of decimal places if it has less decimal places than the specified number
amountPerPerson = round((totalInteger * (1 + (tipPercentageInteger/100))) / peopleCountInteger, 2)

amountPerPerson = "{:.2f}".format(amountPerPerson)
print(f"Each person should pay: $ {amountPerPerson}")