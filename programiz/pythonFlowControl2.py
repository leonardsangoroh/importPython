########################################if statement############################################
age = 18

if age > 18:
    print('You are okay')

print('Kumbe ni under 18')

#####################################if else statement#########################################
if age > 3:
    print('They can start school')
else:
    print('Let the child stay at home')

print('Follow the ruling made above')

###################################if..elif..else statement######################################
number = 0

if number > 0:
    print("Positive number")

elif number == 0:
    print('Zero')
else:
    print('Negative number')

print('This statement is always executed')

########################################nested if############################################
# outer if statement
if (number >= 0):
    # inner if statement
    if number == 0:
      print('Number is 0')
    
    # inner else statement
    else:
        print('Number is positive')

# outer else statement
else:
    print('Number is negative')

# Output: Number is positive
