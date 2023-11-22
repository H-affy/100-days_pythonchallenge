"""fruits = ["Apple", "Orange", "Avocado"]

for fruit in fruits:
    print(fruit)
    print(fruit + "pie")
print(fruits)"""

"""# Calculating the average using loop
student_heights = input("Enter student height: ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])

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

# Checking for maximum score using loop
student_scores = input("Input student scores: ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])

highest_score = 0
for score in student_scores:
  if score > highest_score:
    highest_score = score
print(f"The highest score in the class is: {highest_score}")

total = 0
for number in range(1, 101):
    total += number
print(total)"""



number = 0
for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 5 == 0:
        print("Buzz")
    elif i % 3 == 0:
        print("Fizz")
    else:
        print(i)