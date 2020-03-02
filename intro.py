print("Testing..")
a = 4
b = 7
c_squared = a**2 + b**2
c = c_squared ** (1/2)
print(c)
import math
print(math.sqrt(c_squared))
username = input("Give me your username?")
print("Your username is," , username)
if username =="admin":
    print("admin")
else:
    print("ANAM")

num = int(input("Type a number here: "))
if (num % 2) == 0:
    print(num, "even")
if (num % 3) == 0:
    print(num, "odd")
    for x in range(10):
        print(x)

i=1
while i <= 100:
    if i%3==0:
        print("Fizz", end="")
        if i%5==0:
            print("Buzz", end="")
    elif i%5==0:
        print("Buzz", end="")
    else:
        print(i, end="")
    print()
    i+=1