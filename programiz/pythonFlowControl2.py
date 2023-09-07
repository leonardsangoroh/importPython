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

########################################for loop############################################

#loops - used to repeat a block of code
languages = ['Swift','Python','SQL']

for language in languages:
    print(language)

for x in 'Python':
    print(x)

##################################for loop with python range####################################
values = range(4)

for i in values:
    print(i)

#############################for loop without accessing items###############################
for language in languages:
    print('Hello')
    print('Leonard')
    #the output prints 'Hello' and 'Leonard' 3 times
    #we did not necessarily print the items of the list

#if the items of a sequence is not to be used, the loop can be written as follows
for _ in language:
    print("Hello Leonard")

#############################for loop wit else###############################
#the else part is executed after the loop iterates through every item of a sequence
digits = [0,3,6]

for i in digits:
    print(i)
else:
    print('No items left')