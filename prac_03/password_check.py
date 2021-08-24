
char_length = 10
while True:
    password = input("Enter a password at least {} characters long: ".format(char_length))
    if len(password) < char_length:
        continue
    else:
        for i in range(0, len(password)):
            print("*", end="")
        break





