# Scout Crooke, 10/09/19, this program gives the user practice math problems

import random


def get_max_num():
    max_num = float(input("What is the maximum you would like?"))
    return max_num


def get_problem_type():
    problem_type = float(input("What type of problem would you like?"))
    return problem_type

def main():
    maximum = get_max_num()
    problem = get_problem_type()
    random.randint(0, maximum)
    if problem == "+":
        print("User picked addition")


main()

