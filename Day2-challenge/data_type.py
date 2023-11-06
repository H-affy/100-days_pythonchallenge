two_digit_number = input("Enter yor number: ")
first_digit = int(two_digit_number[0])
second_digit = int(two_digit_number[1])
two_digit_number = (first_digit + second_digit)
print(two_digit_number)

#Mathematical operations
#Create a BMI calculator using type conversion and mathematical operations
height = input("Enter your height in meters:\n")
weight = input("Enter your weight in kilograms:\n")
#convert the height and weight using the float and int type conversion.
Height = float(height)
Weight = int(weight)
#using mathematical operation to calculate the bmi
bmi = Weight/Height ** 2
#using the round function to round to whole number
BMI = round(bmi)
print(BMI)