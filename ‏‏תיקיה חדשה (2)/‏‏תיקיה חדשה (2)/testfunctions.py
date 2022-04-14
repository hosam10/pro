def check_if_input_is_valid(user_input: int) -> bool:
    """
    function checks if users input is valid
    :param user_input: the value that the users enter
    :return: true if the input is valid
    """
    return isinstance(user_input, int) and user_input < 3 and user_input > 0


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


def print_file_sorted(file_content: list) -> None:
    """
    function prints the txt file content in a sorted way
    :param file_content: the content of the txt file
    :return: the function dont returns it just prints the content of the txt file in a sorted way
    """
    needed_words_to_print = ["id", "name", "quantity"]#list of  words that we wan to print

    for line in file_content:
        index = 0
        splited_line = line.split(":")
        for lines_index in splited_line:
            print("product", needed_words_to_print[index], ":", lines_index)
            index = index + 1


def print_prodtctid_quantity_less_than_10_and_there_count(file_content: list) -> None:
    """
    function prints all products id that have less quantity than 10 and the amount of products that have less quantity than 10
    :param file_content: the content of the txt file
    :return: the function dont returns it just prints all products id that have less quantity than 10 and the amount of products that have less quantity than 10

    """
    count_of_produts = 0
    for line in file_content:
        splited_line = line.split(":")
        if int(splited_line[ - 1]) < 10:
            count_of_produts +=  1
            print("product that its quanitity less than 10 id:",splited_line[0])
    print("there is ",count_of_produts," products have a quantity less than 10")



def exiting_out_of_program()->None:
    """
    function that prints that the uuser is exiting out of the program
    :return:  function dont retutn just prints
    """
    print("Thank you for using our program. exiting from the application")



def use_program()->None:
    """
    using the program
    """
    try:
        user_input=int(input("enter one  number from 1 to 3\n if you enterd1:prints the txt file content in a sorted way"
                  "\n if you enters2:prints all products id that have less quantity than 10 and the amount of products that have less quantity than 10"
                  "\nif you enterd3:exit out of the program "))
        if not isinstance(user_input,int):
            raise TypeError

        if user_input<1 or user_input >3:
            raise ValueError
        if user_input ==1:
            print_file_sorted(get_file_contents("products.txt"))
        if user_input ==2:
            print_prodtctid_quantity_less_than_10_and_there_count(get_file_contents("products.txt"))
        if user_input == 3:
                exiting_out_of_program()
    except TypeError:
        raise TypeError("you should enter a integer number")
    except ValueError:
        raise ValueError ("you should enter a number between 1 and 3")

