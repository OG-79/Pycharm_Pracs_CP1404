# CP1404/CP5632 - Practical
# Answer the following questions:
# 1. When will a ValueError occur? When the input is not an integer number
# 2. When will a ZeroDivisionError occur? When dividing a number by zero
# 3. Could you change the code to avoid the possibility of a ZeroDivisionError? I have updated the provided code


try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    if denominator == 0:
        print("The answer is undefined")
    else:
        fraction = numerator / denominator
        print(fraction)
    print("Finished.")
except ValueError:
    print("Numerator and denominator must be valid numbers!")














