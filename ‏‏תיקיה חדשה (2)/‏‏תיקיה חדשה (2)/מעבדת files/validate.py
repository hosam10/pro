def check_integer_in_range(integer_to_check: int, bottom_range_value: int, top_range_value: int) -> bool:
    """
    Functino checks if the given integer is at the specified range
    :param integer_to_check: Integer value to check
    :param bottom_range_value:  Bottom range value to check with
    :param top_range_value: Top range value to check with
    :return: True if the given integer is at the specified range and False otherwise
    """
    return all(isinstance(parameter, int) for parameter in
               locals().values()) and bottom_range_value <= integer_to_check <= top_range_value
