def get_file_contents(file_path: str) -> list:
    """
    File is responsible to get the file contents and return it as a single string list
    :param file_path: A path of a file to read the contents from
    :return: List where each element represents the file's single line
    :raise FileNotFoundError If a file we want to read from doesn't exist
    :raise PermissionError If a file we want to read from exists but we don't have permissions read its contents
    """
    try:
        with open(file_path, 'r') as f:
            return f.read().splitlines()
    except FileNotFoundError:
        raise FileNotFoundError("File can't be found.")
    except PermissionError:
        raise PermissionError("You don't have the permissions to read its content")


def is_integer_value_in_file(value_to_find: int, file_to_search_at: str) -> bool:
    """
    Function checks if one of the file's lines is equal to the given integer
    :param value_to_find: Integer value to search for at the given text file
    :param file_to_search_at: The file to search at
    :return: True if the given integer exists at the file and False otherwise
    :raise FileNotFoundError A utility function the current function uses raises this exception if a file we want to read from doesn't exist
    :raise PermissionError A utility function the current function uses raises this exception if a file we want to read from exists but we don't have permissions read its contents
    """
    return isinstance(value_to_find, int) and isinstance(
        file_to_search_at,
        str) and str(value_to_find) in get_file_contents(file_to_search_at)
