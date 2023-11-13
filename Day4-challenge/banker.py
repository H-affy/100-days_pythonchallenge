Names = input("Enter the names. Separate with comma: ").split(", ")

import random
name = len(Names)

random_name = random.randint(0, name - 1)
print(random_name)
names = Names[random_name]
print(f"{names} is buying the meal.")