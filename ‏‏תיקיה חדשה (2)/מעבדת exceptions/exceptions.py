def get_positive_list_index() -> int:
    """
    Function gets a positive list index
    :raises ValueError if the user's input is not a positive integer number
    :return: Returning a positive list index value we've got from the user if it is valid
    """
    try:
        positive_list_index = int(input("Enter a positive index to get list element of:"))
        if positive_list_index < 0:
            raise ValueError

        return positive_list_index
    except ValueError:
        raise ValueError("Not a positive integer number")


def get_list_element_by_index(list_to_get_from: list, element_index: int):
    """
    Function gets a value of the specific list's element (by the given index)
    :raises TypeError if the given object is not a list
    :raises IndexError if the passed index is out of boundaries
    :param list_to_get_from: List to get the element's value from
    :param element_index: Element's positive index
    :return: The value of the specific list's element (by the given index)
    """
    try:
        if not isinstance(list_to_get_from, list):
            raise TypeError

        return list_to_get_from[element_index]
    except IndexError:
        raise IndexError("List index is out of bounds")
    except TypeError:
        raise TypeError("You must pass a list to get an element of and an integer index")


"""
The main section
"""
lst = [1, 2, 3, 4, 5, 6]

try:
    print(get_list_element_by_index(lst, get_positive_list_index()))
except IndexError as i:
    print(i)
except ValueError as v:
    print(v)
except TypeError as t:
    print(t)
