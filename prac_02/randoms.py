import random

print(random.randint(5, 20))
print(random.randrange(3, 10, 2))
print(random.uniform(2.5, 5.5))
# Line 1, the output had positive integers, the smallest number that could have been seen is 5, and the largest
# number that could have been seen is 20
# Line 2, numbers between 3 and 10 and each were incremented by 2. The smallest number that could be seen is 3,
# and the largest number 9
# Line 3, each output had decimal numbers that never went below 3 and only once a number greater than 5 got
# displayed

lowest = 0
highest = 100

random_number = random.randint(lowest, highest)
print(random_number)
