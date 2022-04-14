from math import prod
from checkings import *


def hack_execution(numbers_to_hack: list, tries_amount: int, bottom_range_number: int, top_range_number: int) -> None:
    """
    The current function is the main program execution function
    :param bottom_range_number:
    :param numbers_to_hack: List which contains numbers to guess
    :param tries_amount: An amount of guesses
    :param bottom_range_number: bottom range value to check with
    :param top_range_number: top range value to check with
    :return: Nothing to return
    """
    # If the tries amount or numbers to hack list is/are not valid
    if not check_positive_integer(tries_amount) or not check_positive_integer(
            bottom_range_number) or not check_positive_integer(top_range_number):
        return

    guess_times = 0  # An amount of guesses the user has made

    while True:
        # If the user has failed to guess the combination correctly
        if guess_times == tries_amount:
            print("You have failed! FBI is coming to get you")
            break

        # Displaying the hint message
        if not hack_display_hint(numbers_to_hack, bottom_range_number, top_range_number):
            print("Program error. Wrong numbers list is given!")
            break

        # If the user has guessed the combination
        if handle_user_guess(numbers_to_hack, bottom_range_number, top_range_number):
            break

        guess_times += 1

        print(f"You have {tries_amount - guess_times} more tries")


def handle_user_guess(numbers_to_hack: list, bottom_range_number: int, top_range_number: int) -> bool:
    """
    Function executes the specific code, according to the user's guess
    :raises ValueError This exception is thrown if the user's input is invalid
    :return: True if the user guessed the combination and False otherwise
    """
    try:
        # Getting the combination's values and checking with the original combination
        if compare_lists([int(input("")) for _ in range(len(numbers_to_hack))], numbers_to_hack, bottom_range_number,
                         top_range_number):
            print("You are in! Be quick before FBI catches you!")
            return True
        else:
            print("Wrong number list is given or wrong combination")
            return False
    except ValueError:
        raise ValueError("You need to enter numerical values only")


def hack_display_hint(numbers_to_hack: list, bottom_range: int, top_range: int) -> bool:
    """
    Function displays a hint for numbers to guess
    The function displays there multiply and summary
    :param numbers_to_hack: List which contains the numbers to guess
    :param bottom_range: bottom range value to check with
    :param top_range: top range value to check with
    :return: True if the given list is correct and the message must be displayed and False otherwise
    """
    if not check_integers_in_range_list(numbers_to_hack, bottom_range, top_range):
        return False

    print("""
    You are a secret agent breaking into a server room
    There are""", len(numbers_to_hack), """numbers you need to enter for the locked door to open
    The codes digits multiply to give:""", prod(numbers_to_hack), """
    The codes digits summarize to give:""", sum(numbers_to_hack), """
    Enter three digits to guess the secret access code    
    """)

    return True
