# Hosam abuelhiga - 322507880
# Qusai majle - 323004200

def check_input_starting_number_integer_6_or_2(starting_number: int) -> bool:
    """
    # The function returns true if the startingNumber given as parameter
    is integer and equals 6 or 2 else returns false

    :param starting_number: startingNumber to check
    :return: True if the startingNumber is integer
    and equals 2 or 6 else return false
    """

    if isinstance(starting_number, int) and starting_number == 2 or starting_number == 6:
        return True
    else:
        return False


def build_cards_deck(starting_number: int) -> dict:
    """
    :param starting_number: the startingNumber has to be integer number and equal 6 or 2
    :return: if the startingNumber equals 2 return full cardsDeck ,
    if the startingNumber equals 6 return 6 and above cardsDeck
    else return empty dictionary
    """
    list_of_cards_for_the_starting_number2 = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A']  # full cardsDeck
    list_of_cards_for_the_starting_number6 = [6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A']  # 6 and above cardsDeck
    cards_deck = {}  # empty dictionary

    pips = ['♡', '♣', '♢', '♠']  # Keys for cardsDeck dictionary

    # check if the starting number is integer and equal 2 or 6
    if check_input_starting_number_integer_6_or_2(starting_number):
        if starting_number == 2:
            """
            inserting the pips of the cards deck('♡', '♣', '♢', '♠') as keys for are dictionary(cardsDeck) 
            and entering for each key the full deck
            """
            cards_deck = dict.fromkeys(pips, list_of_cards_for_the_starting_number2)
            return cards_deck

        if starting_number == 6:
            """
            inserting the pips of the cards deck('♡', '♣', '♢', '♠') as keys for are dictionary(cardsDeck) 
            and entering for each key the 6 and above cardsDeck
            """
            cards_deck = dict.fromkeys(pips, list_of_cards_for_the_starting_number6)
            return cards_deck
    else:
        return cards_deck  # if the startingNumber is not correct return empty dictionary


def check_cards_decks_keys(cards_deck: dict) -> bool:
    """

    :param cards_deck: the cardsDeck has to be dict and check if its keys are equal to cards pips
    :return: True if the keys equals cards pips else False
    """
    if isinstance(cards_deck, dict):  # Check if the cardsDeck is from the type dictionary
        pips = ['♡', '♣', '♢', '♠']  # Keys for cardsDeck dictionary
        if isinstance(pips, list):  # Check if the keys is from the type list
            pips_index = 0
            for key in cards_deck.keys():  # loop in the dictionary  cardsDeck keys
                if key != pips[pips_index]:  # False if the key for cardsDeck is NOT equal with cardSymbol
                    return False
                pips_index = pips_index + 1
            return True  # the loop has ended and all the keys are proper
        else:
            return False  # if the pips list is not a list type
    else:
        return False  # if the value is not a dictionary type


def check_pip_cards_when_the_inputs_starting_number_is2(cards_deck: dict) -> bool:
    """

    :param cards_deck: the cardsDeck has to be dict
    and check if the cardsDeck is proper(to what's ordered in startingNumber=2)
    :return: true if the value is proper  else false
    """
    proper_list_of_cards_for_the_starting_number2 = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A']  # proper full cardsDeck

    if isinstance(cards_deck, dict):  # Check if the cardsDeck is from the type dictionary
        for pipCards in cards_deck.values():  # loop in the dictionary cardsDeck(value of every part)
            if isinstance(pipCards, list):  # check if all the parts is instance of list
                if pipCards != proper_list_of_cards_for_the_starting_number2:  # check if the value of the  parts is proper
                    return False  # the value of this part is not proper

            else:
                return False  # the value of this part is not instance of list
        return True  # the loop has ended and all the values in cardsDeck are proper
    else:
        return False  # the cardsDeck(inputted value) is not a dictionary type


def check_pip_cards_when_the_inputs_starting_number_is6(cards_deck: dict) -> bool:
    """
    :param cards_deck: the cardsDeck has to be dict
    and check if the cardsDeck is proper(to what's ordered in startingNumber=6)
    :return: true if the cardsDeck is proper  else false
    """
    proper_list_of_cards_for_the_starting_number6 = [6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A']  # proper 6 and above cardsDeck
    if isinstance(cards_deck, dict):  # Check if the cardsDeck is from the type dictionary
        for pipCards in cards_deck.values():  # loop in the dictionary cardsDeck(value of every part)
            if isinstance(pipCards, list):  # check if all the parts is instance of list
                if pipCards != proper_list_of_cards_for_the_starting_number6:  # check if the value of the parts  is proper
                    return False  # the value of this part is not proper

            else:
                return False  # the value of this part is not instance of list
        return True  # the loop has ended and all the values in cardsDeck are proper
    else:
        return False  # the cardsDeck(inputted value) is not a dictionary type


def cards_decks_new_display(cards_deck: dict, starting_number: int) -> None:
    """

    :param cards_deck: the value has to be dict
    and check if the value is proper(in terms of keys and value of each part)
       :param starting_number:the startingNumber has to be integer number and equal 6 or 2
       the function displays the cards deck in a more convenient format for the user
       """

    # checking if the starting number is proper (integer and its value is 6 or2)
    if check_input_starting_number_integer_6_or_2(starting_number):
        if check_cards_decks_keys(cards_deck):  # checking the keys in cardsDecks if its proper.
            """ checking the cardsDecks parts values if its proper in range 6 and the starting number is 6
                or if its proper in range 2 and the starting number is 2"""
            if starting_number == 6 and check_pip_cards_when_the_inputs_starting_number_is6(cards_deck) \
                    or starting_number == 2 and check_pip_cards_when_the_inputs_starting_number_is2(cards_deck):
                for key, value in cards_deck.items():  # printing the cards deck
                    print(key, ":", value)
            else:
                print("The values is not correct")
        else:
            print("The keys is not correct")
    else:
        print("the starting number is incorrect ")