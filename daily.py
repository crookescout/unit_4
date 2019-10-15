# by Scout Crooke, 10/3/19, this program does daily exercises

import random

# num = float(input("What is the number?"))
#
# if num % 2 == 0:
#     print("This is an even number")
# else:
#     print("This is an odd number")


def is_divisible(num, check):
    if num % check == 0:
        return True
    else:
        return False


def is_triangle(s1, s2, s3):
    if s1 >= s2 + s3:
        return False
    elif s2 >= s1 + s3:
        return False
    elif s3 >= s2 + s1:
        return False
    else:
        return True


def computer():
    return random.randint(1, 3)


def rock_paper_scissors():
    user_choice = input("Let's play rock-paper-scissors! Choose one!")
    computer_choice = computer()
    if computer_choice == 1:
        print("Computer chose rock")
        if user_choice == "rock":
            print("Tie!")
        elif user_choice == "scissors":
            print("You win!")
        else:
            print("Sorry, you lose!")
    if computer_choice == 2:
        print("Computer chose paper")
        if user_choice == "paper":
            print("Tie!")
        elif user_choice == "rock":
            print("You win!")
        else:
            print("Sorry, you lose!")
    if computer_choice == 3:
        print("Computer chose scissors")
        if user_choice == "scissors":
            print("Tie!")
        elif user_choice == "paper":
            print("You win!")
        else:
            print("Sorry, you lose!")


def caught_speeding(speed, birthday):
    if birthday:
        speed -= 5
    if speed <= 60:
        return 0
    elif speed >= 61 and speed <= 80:
        return 1
    else:
        return 2



def main():
    # num = float(input("What is the first number?"))
    # check = float(input("What is the second number?"))
    # if is_divisible(num, check):
    #     print("Yes,", num, "is divisible by", check)
    # else:
    #     print("No,", num, "is not divisible by", check)
    #
    # s1 = float(input("What is the length of side #1?"))
    # s2 = float(input("What is the length of side #2?"))
    # s3 = float(input("What is the length of side #3?"))
    # if is_triangle(s1, s2, s3):
    #     print("Yes")
    # else:
    #     print("No")
    #
    # computer()
    # rock_paper_scissors()

    print(caught_speeding(65, True))


main()




