def check_positive_integer(integer_to_check: int) -> bool:
    """
    Function checks if the given value is a positive integer
    :param integer_to_check: Value to check
    :return: True if the given value is a positive integer and False otherwise
    """
    return isinstance(integer_to_check, int) and integer_to_check > 0


def check_not_empty_list(list_to_check: list) -> bool:
    """
    Function checks if the given element is a list which contains at least one element
    :param list_to_check: reference to an object we will check
    :return: True if the given element is a list which contains at least one element and False otherwise
    """
    return isinstance(list_to_check, list) and list_to_check != []


def check_integers_in_range_list(list_to_check: list, bottom_range: int, top_range: int) -> bool:
    """
    Function checks if the given list contains only integers from the given range
    :param list_to_check: list to check
    :param bottom_range: bottom range value to check with
    :param top_range: top range value to check with
    :return: True if the given list contains only integers at the given range and False otherwise
    """
    return check_not_empty_list(list_to_check) and all(
        isinstance(element, int) and bottom_range <= element <= top_range for element in list_to_check)


def compare_lists(user_guess_numbers: list, numbers_to_hack: list, bottom_range: int, top_range: int) -> bool:
    """
    Function checks if both lists are identical
    :param user_guess_numbers: The list contains numbers the user guessed
    :param numbers_to_hack: The list contains the numbers to guess
    :param bottom_range: bottom range value to check with
    :param top_range: top range value to check with
    :return: True if both lists are identical and False otherwise
    """
    return check_integers_in_range_list(user_guess_numbers, bottom_range, top_range) and check_integers_in_range_list(
        numbers_to_hack, bottom_range, top_range) and user_guess_numbers == numbers_to_hack
