from hack_numbers_handler import hack_execution
from random import randint

if __name__ == "__main__":
    amount_of_digits = 3
    tries_amount = 3
    bottom_range_value = 1
    top_range_value = 9

    try:
        hack_execution([randint(bottom_range_value, top_range_value) for i in range(amount_of_digits)], tries_amount,
                       bottom_range_value,
                       top_range_value)
    except ValueError as v:
        print(v)
