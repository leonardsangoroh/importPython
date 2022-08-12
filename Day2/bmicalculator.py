height = input("Enter your height in m: ")
weight = input("Enter your weight in kg: ")


heightFloat = float(height)
weightInt = int(weight)

heightSquared = heightFloat ** 2

bmi = weightInt/heightSquared

#convert to integer
print(int(bmi))