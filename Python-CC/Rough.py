#
enterNumber = input("Please enter a number, and i'll tell you if it's divisible by 10: ")
enterNumber = int(enterNumber)

if enterNumber % 10 == 0:
    print(f"{enterNumber} is divisible by 10")
else:
    print(f"{enterNumber} isn't divisible by 10")