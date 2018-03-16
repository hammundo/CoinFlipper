import random

while True:
    print("How many times do you want to flip the coin?")
    try:
        flip_count = int(input())
        if flip_count < 1:
            print("Input must be a positive integer. Please try again.")
            continue
        break
    except ValueError:
        print("Input not recognised. Please only enter positive integers.")

head_count = 0
tails_count = 0

print("Coin flipper starting!\nFlipping coin ", flip_count, " times.")

for i in range(1, flip_count + 1):
    print("Flip #", i)
    coin_toss = random.choice([True, False])

    if coin_toss:
        print(" Heads!")
        head_count = head_count + 1
        i = i + 1
    else:
        print(" Tails!")
        tails_count = tails_count + 1
        i = i + 1

try:
    head_percentage = head_count / flip_count * 100
    tails_percentage = 100 - head_percentage
except ZeroDivisionError:
    print("Cannot divide by 0!")

print("\nNumber of times landed on head:", head_count, "(", head_percentage, "%)")
print("Number of times landed on tails:", tails_count, "(", tails_percentage, "%)")
