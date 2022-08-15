#f-string

# why f-string?
# because the print() function cannot accept 2 different data types as arguments

score = 0
height = 1.8
isWinning = True

#fstring
print(f"My score is {score}, and my height is {height}")

# coding exercise
# program that tells us how many days, weeks, months we have left
# Assuming we live until 90 years old

ageLimit = 90
oneYearDays = 365
oneYearWeeks = 52
oneYearMonths = 12

age = input("What is your current age? ")

ageInteger = int(age)

remainingYears = ageLimit - ageInteger
remainingDays = remainingYears * oneYearDays
remainingWeeks = remainingYears * oneYearWeeks
remainingMonths = remainingYears * oneYearMonths

print(f"You have {remainingDays} days, {remainingWeeks} weeks, and {remainingMonths} months left")
