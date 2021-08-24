
# for loop that displays all of the odd numbers between
# 1 and 20 with a space between each one.
for i in range(0, 21, 2):
    print(i, end=' ')
print()

# a.) for loop to count in 10s from 0 to 100
for i in range(0, 101, 10):
    print(i, end=' ')
print()

# b.) for loop to count down by 1 from 20 to 1
for i in range(21, 0, -1):
    print(i, end=' ')
print()

# c.) print n stars. Ask the user for a number, then print that many stars (*), all on one line
number_of_stars = int(input("Number of stars: "))
for i in range(number_of_stars):
    print('*', end=' ')
print()

# d.) print n lines of increasing stars.
# using the same number as above print lines of increasing stars, starting at 1 and increasing by 1
for i in range(1, number_of_stars + 1):
    print('*' * i)
print()
