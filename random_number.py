from random import randint


def roll():
    return randint(1, 6)


# Exercise 2
# Simulate 10,000 rolls of a die and display the average number rolled.
num_rolls = 10_000
total = 0

for trial in range(num_rolls):
    total = total + roll()
    # print(total)

avg_roll = total / num_rolls

print(f"The average result of {num_rolls} rolls is {avg_roll}")
