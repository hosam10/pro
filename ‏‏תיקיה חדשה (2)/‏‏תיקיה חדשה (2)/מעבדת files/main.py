from validate import check_integer_in_range
from files_handler import is_integer_value_in_file

if __name__ == "__main__":
    bottom_range = 100000
    top_range = 999999
    file_path = "1.txt"
    try:
        # Getting an integer number to search for at the specific text file
        value_to_search_for = int(input(f"Enter a number between {bottom_range} and {top_range}:"))

        # Checking if the given number is valid and exists at the given text file
        if check_integer_in_range(value_to_search_for, bottom_range, top_range):
            print("Does", value_to_search_for, "exists at the file?",
                  is_integer_value_in_file(value_to_search_for, file_path))
        else:
            print(f"Your value must be an integer value and must between {bottom_range} and {top_range}")
    except ValueError:  # If we are given something that cn't be casted to integer
        print("You must enter an integer value to search for at the file")
    except FileNotFoundError as f:  # If the text file doesn't exist
        print(f)
    except PermissionError as p:  # If the text file exists but we don't have permission to read from that file
        print(p)
