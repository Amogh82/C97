import random
n = random.randint(1 , 9)
for i in range(1 , 6):
    y = input("Enter your guess: ")
    x = int(y)
    if x > n:
        print("Too high")
    if x < n:
        print("Too low")
    if x == n:
        print("That's correct")
        break