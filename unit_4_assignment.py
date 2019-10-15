# Scout Crooke, 10/09/19, this program gives the user practice math problems

import random


def get_max_num():
    """
    This function gets the user's maximum number which could be a decimal
    :return: maximum number as a float
    """
    max_num = float(input("What is the maximum you would like?"))
    return max_num


def get_problem_type():
    """
    This function gets the user's type of math problem and if the user does not type one of the specific types of
    problems, it will automatically become an addition problem
    :return: type of problem as a string
    """
    problem_type = str(input("What type of math problem would you like? (*, -, or +)"))
    return problem_type


def compare_answers(user_answer, correct_answer):
    """
    This function compares the user's answer with the correct answer and tells the user if they got the problem correct
    :param user_answer:
    :param correct_answer:
    :return: none
    """
    if user_answer == correct_answer:
        print("Great work! You got the correct answer!")
    else:
        print("Sorry, that is not the correct answer")


def main():
    maximum = get_max_num()
    problem = get_problem_type()
    random1 = random.randint(0, maximum)
    random2 = random.randint(0, maximum)
    if problem == "*":
        print("User picked multiplication. Here is the problem:", random1, "*", random2)
        user_answer = float(input("What is the answer to this problem?"))
        compare_answers(user_answer, random1 * random2)
    elif problem == "-":
        print("User picked subtraction. Here is the problem:", random1, "-", random2)
        user_answer = float(input("What is the answer to this problem?"))
        compare_answers(user_answer, random1 - random2)
    else:
        print("User picked addition. Here is the problem:", random1, "+", random2)
        user_answer = float(input("What is the answer to this problem?"))
        compare_answers(user_answer, random1 + random2)
    print("Thanks for playing!")


main()
