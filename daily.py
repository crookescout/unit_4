# by Scout Crooke, 10/3/19, this program does daily exercises

num = float(input("What is the number?"))

if num % 2 == 0:
    print("This is an even number")

else:
    print("This is an odd number")


def is_divisible(num, check):
    if num % check == 0:
        return True
    else:
        return False


def main():
    num = float(input("What is the first number?"))
    check = float(input("What is the second number?"))
    if is_divisible(num, check):
        print("Yes,", num, "is divisible by", check)


main()