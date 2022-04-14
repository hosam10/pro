def display_message(message_to_display: str) -> None:
    """
    Function displays the given message
    :param message_to_display: Message to display
    :return: None
    """
    print(message_to_display)


# display_message("Hello World!")
# display_message("Goodbye world!")

# def sum_two_integers(first_integer, second_integer):
#     return first_integer + second_integer

# def func():
#     return 1, 2, 3
#
#
# print(type(func()))
#
# a = func()
# print(type(a), a)
#
# a, b, c = func()
# print(type(a), type(b), type(c), a, b, c)


# def display_full_name(first_name="Avi", last_name="Cohen"):
#     print(first_name, last_name)
#
#
# display_full_name()
# display_full_name("Kobi")
# display_full_name("Kobi", "Levi")
# display_full_name(last_name="Levi", first_name="Kobi")


# def get_full_name(first_name="Avi", last_name="Cohen"):
#     """
#     Function return full name, according to given first and last names
#     :param first_name: First name to use at the full name value
#     :param last_name: Last name to use at the full name value
#     :return: Returns a full name, according to given first and last names
#     """
#     return first_name+" "+last_name

def in_range(number_to_check: int, bottom_range_value: int, top_range_value: int) -> bool:
    """
    Function checks if the given value is at the specific range
    :param number_to_check: Number to check
    :param bottom_range_value: The bottom range value to compare the number with
    :param top_range_value: The top range value to compare the number with
    :return: True if the given number is at the range and False otherwise
    """
    print(locals().values())
    return all(isinstance(parameter, int) for parameter in
               locals().values()) and bottom_range_value <= number_to_check <= top_range_value


print(in_range(3, 1, 11))
