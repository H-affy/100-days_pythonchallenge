print("The Love Calculator is calculating your score...")
name1 = input("What is your name?\n")
name2 = input("What is their name?\n")

#combining the names
name = name1 + name2

#convert the name to lowercase
names = name.lower()

#Using the count function to count many time each letter occurs
t = names.count("t")
r = name.count("r")
u = name.count("u")
e = names.count("e")

TRUE = t + r + u + e
true = str(TRUE)

l = names.count("l")
o = names.count("o")
v = names.count("v")
e = names.count("e")

LOVE = l + o + v + e
love = str(LOVE)

lovescores = true + love
print(lovescores)

lovescore = int(lovescores)

if lovescore < 10 or lovescore > 90:
    print(f"Your score is {lovescore}")