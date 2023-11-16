"""fruits = ["Apple", "Orange", "Avocado"]

for fruit in fruits:
    print(fruit)
    print(fruit + "pie")
print(fruits)"""

# Input a Python list of student heights
student_heights = input("Enter student height: ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆
  
# Write your code below this row 👇
total_height = 0
for height in student_heights:
  total_height += height
print(total_height)

number_of_student = 0
for number in student_heights:
  number_of_student += 1
print(number_of_student)

average_height = total_height / number_of_student
average_height = round(average_height)
print(average_height)