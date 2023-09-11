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

########################################while loop############################################

#program to display numbers from 1 to 5

i = 1
n = 5

while i<n:
    print(i)
    i = i + 1

#example two
total = 0

number = int(input("Enter a number: "))

#add numbers until number is zero
while number != 0:
    total += number

    number = int(input("Enter a number"))

print('total = ', total)

###################################infinite while loop#######################################
#age = 32

#while age > 18:
#    print('Go and vote')

###################################while loop with else#######################################
#the else block is executed it the while loop is terminated by a break statement

counter = 0

while counter < 3:
    if counter == 1:
        break
    
    print('inside loop')
    counter = counter +1
else:
    print('Inside else')

###################################break & continue#######################################
#used to terminate a loop immediately when its encountered

#used to terminate a for loop when a certain condition is met
for i in range(5):
    if i == 3:
        break
    print(i)

#used to terminate a while loop
ii = 1

while ii<=10:
    print('6 * ', (ii), '=', 6*i)

    if ii >=5:
        break
    ii = i + 1


#continue statement is used to skip the current iteration of the loop and the control flow of
# the program goes to the next iteration
for k in range(5):
    if k == 3:
        continue
    print(k)

###################################pass statement#######################################
# the pass statement is a null statemnt that can be used as a placeholder for future code
nn = 10

if nn>10:
    pass

print('Hello')

def function(args):
    pass

class Example:
    pass