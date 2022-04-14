# Osama Arfaeh 326836277
# Shiran Mazuz 207851122
# 46.1

# ex1
def check_input_integer_6_or_2(number_start_values: int) -> bool:
    """
    Function Checks that the input is an integer and that its value is either 2 or 6
    :param number_start_values: number start values
    :return: bool
    """
    return isinstance(number_start_values, int) and (number_start_values == 6 or number_start_values == 2)


def build_deck_of_cards(number_start_values: int) -> dict:
    """
    Function build deck of cards
    :param number_start_values: number start values
    :return: dict
    """
    deck_of_cards = {}
    # list of desired keys
    list_of_key = ["♡", "♣", "♢", "♠"]
    # list of desired letters values
    list_of_letter = ["J", "Q", "K", "A"]
    # a new empty list for fill it in a range from the number start values and after that add the desired list letter
    list_of_number = []
    if check_input_integer_6_or_2(number_start_values):
        for i in range(number_start_values, 11):
            list_of_number.append(i)
        # extend - adds all the elements of an iterable (list, tuple, string etc.) to the end of the list.
        list_of_number.extend(list_of_letter)
        # fill in the dictionary
        for j in list_of_key:
            deck_of_cards[j] = list_of_number
    return deck_of_cards


# ex2
def check_if_value_in_the_dictionary_is_list(deck_of_cards: dict) -> bool:
    """
    Function checks if value in the dictionary is list
    :param deck_of_cards: dictionary deck of cards
    :return: bool
    """
    for value in deck_of_cards.values():
        if not isinstance(value, list):
            return False
    return True


def check_input_keys_of_dictionary(deck_of_cards: dict) -> bool:
    """
    Function Checks that the input is a dictionary and that his keys is kind of card
    :param deck_of_cards: dictionary deck of cards
    :return: bool
    """
    # list of desired keys
    list_of_key = ["♡", "♣", "♢", "♠"]
    # checks the keys of the deck of cards
    for key in deck_of_cards.keys():
        if not key in list_of_key:
            return False
    return True


def check_input_list_dictionary(deck_of_cards: dict, number_start_values: int) -> bool:
    """
    Function Checks the input list value of dictionary
    :param deck_of_cards: dictionary deck of cards
    :param number_start_values: number start values
    :return: bool
    """
    # checks the input of number start values
    if not check_input_integer_6_or_2(number_start_values):
        return False
    # create a standard deck of cards
    new_dictionary = build_deck_of_cards(number_start_values)
    # save one of a list value from the standard deck of cards
    new_list = new_dictionary["♡"]
    # check if the lists in our deck of card are correct
    for value in deck_of_cards.values():
        if value != new_list:
            return False
    return True


def deck_conveniently_to_the_user(deck_of_cards: dict, number_start_values: int) -> None:
    """
    Function that displays the deck conveniently to the user
    :param deck_of_cards: dictionary deck of cards
    :param number_start_values: number start values
    :return: None
    """
    # if the input is correct
    if isinstance(deck_of_cards, dict) and check_input_keys_of_dictionary(
            deck_of_cards) and check_if_value_in_the_dictionary_is_list(deck_of_cards) and check_input_list_dictionary(
        deck_of_cards, number_start_values):
        # print the dictionary
        for key, value in deck_of_cards.items():
            print(key, end="  ")
            for v in value:
                print(v, end="  ")
            print()
    else:
        print("The deck of cards is incorrect!")
