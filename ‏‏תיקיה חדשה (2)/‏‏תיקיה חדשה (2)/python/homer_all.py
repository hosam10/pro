# list functions
# grades = [67, 78, 98, 23, 45, 56, 45]
#
# grades.append(99)  # Adding a new element to the end of the list
# print(grades)  # [67, 78, 98, 23, 45, 56, 45, 99]
#
# print(grades.index(45))  # 4 - displaying an index of the first element which equals to 45
# print(grades.count(45))  # Displaying an amount of elements that that their value is equal to 45
#
# grades.remove(45)  # Removing the first element which value is equal to 45
#
# removed_grade = grades.pop(1)
# print(removed_grade)
#
# print(grades.pop())  # If we haven't defined an index, removing the last element
#
# # Some new methods
# fruits = ['apple', 'banana', 'cherry']
#
# fruits.insert(1, "orange")
# print(fruits)
#
# fruits = ['apple', 'banana', 'cherry']
# fruits.reverse()
# print(fruits)
#
# cars = ['Ford', 'BMW', 'Volvo']
# # cars.sort()
# cars.sort(reverse=True)
# print(cars)
#
# fruits = ['apple', 'banana', 'cherry']
# cars = ['Ford', 'BMW', 'Volvo']
# fruits.extend(cars)
# print(fruits)
################################
# String functions
# #Count appearences
# txt = "I love apples, apple are my favorite fruit"
# x = txt.count("apple")#קמות המילה הזה
# print(x)
#
#
# #Checking if the given string starts/ends with
# txt = "Hello, welcome to my world."
# x = txt.endswith(".")#מסימת בנקודה
# print(x)
#
#
# txt = "Hello, welcome to my world."
# x = txt.startswith("Hello")#מתחילה הבמילה זה
# print(x)
#
#
# #Checking if the given string contains specific characters only
# txt = "ae"
# x = txt.isalnum()#אם יש מספר או מחרוזת בלי משהו אחר כמו , . &
# print(x)
#
#
# txt = "CompanyX"
# x = txt.isalpha()# אם מכילה מספר מחזירה שקר
# print(x)
#
#
# txt = "a50800"
# x = txt.isdigit()# אם רק מספרים מחזיר אמת
# print(x)
#
#
# txt = "hello world!"
# x = txt.islower()#  אם רק אתיות קטנות או סימנים
# print(x)
#
#
# txt = "THIS IS NOW&"
# x = txt.isupper()# אם רק אתיות גדלות או סימנים
# print(x)
#
#
# # Join and split the given string by the specific separator
# my_tuple = ("John", "Peter", "Vicky")
# x = "#".join(my_tuple)#מפריד בין המלים ב#
# print(x)
#
#
# txt = "welcome to the jungle"
# x = txt.split()#מחליף מחרוזת למערך על רווח
# print(x)
#
#
# # Lower case letters become upper case letters and vice versa
# txt = "Hello my FRIENDS"
# x = txt.lower() # מחליף הכול לאתיות קטנות
# print(x)
#
#
# txt = "Hello my friends"
# x = txt.upper()# מחליף הכול לאתיות גדולות
# print(x)

##################################################
# Python Dictionary Comprehension
# original_dictionary = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
# # Double each value in the given dictionary
# # דרך1
# # doubled_values_dictionary = {}
# # for key, value in original_dictionary.items():
# #     doubled_values_dictionary[key] = value * 2
# # דרך2
# doubled_values_dictionary = {key: value * 2 for key, value in original_dictionary.items()}
# print(doubled_values_dictionary)
#
# doubled_keys_dictionary = {key * 2: value for key, value in original_dictionary.items()}
# print(doubled_keys_dictionary)
#
# # if statement[[
# # דרך1
# powered_values_dictionary = {}
# for number in range(10):
#     if number % 2 == 0:
#         powered_values_dictionary[number] = number ** 2
# # דרך2
# # powered_values_dictionary = {number: number ** 2 for number in range(10) if number % 2 == 0}
# print(powered_values_dictionary)
#########################


import random

# print(random.randint(1, 100))

from random import randint, choice

# help('random')
# print(randint(1, 100))
# print(choice([1, 2, 3, 4, 5, 6, 7, 8, 9]))#בוחרת מספר וצורה ראנדום בתוך רשימה

# from random import *
#
# print(randint(1, 100))
#
# from math import *
#
# print(ceil(1.1))#מעגלת מספר לפי מעלה
# print(floor(1.99))#מעגלת מספר לפי מעטה
# print(fabs(-1.678))#מחליפה מי שלילי לחיובי
# print(factorial(5))#1*2*3*4*5 (עצירת של מספר)
# print(pow(2, 3))#חזקה
# print(sqrt(81))#שורש

# from os import system
#
# system('ping 8.8.8.8')


#
#
#
#
#
# fruits_set = {"apple", "banana", "cherry"}
# print(fruits_set)
#
# print(len(fruits_set))
# print(type(fruits_set))
#
# numbers_list = [1, 3, 2, 1, 57, 5, 9, 7, 3, 2]
# print(set(numbers_list))#בלי חזרות
#
# print("banana" in fruits_set)
# fruits_set.add("orange")
#
# tropical_fruits_set = {"pineapple", "mango", "papaya", "cherry"}#ללא חזרות
# fruits_set.update(tropical_fruits_set)
#
# another_fruits_list = ["kiwi", "orange", "kiwi","aaa"]
# fruits_set.update(another_fruits_list)
# print(fruits_set)
# fruits_set.remove("orange")# מוחקת אם זה לא נמצה מחזירה חריגה
#
# fruits_set.discard("apple")#  מחוקת אם נמצה בלי חריגות
# print(fruits_set)


# numbers_set = {1, 422, 22, 77, 9}
# print(sorted(numbers_set))
# numbers_set = {1, 422, 22, 77, 9}
# print(sorted(numbers_set, reverse=True))#מיון בסדר הפוך
#
# # Set functions
# print({1, 2, 3}.intersection({2, 3, 4, 5}))  # {2, 3}
# print({1, 2, 3}.union({2, 3, 4, 5}))  # {1, 2, 3, 4, 5}
# print({1, 2, 3}.symmetric_difference({2, 3, 4, 5}))  # {1, 4, 5}


#########################################
# except
# try:
#     age = int(input("Enter your age"))
#     print("Your age is:", age)
# except ValueError:
#     print("Your age must contain digits only")

# try:
#     my_list = ["abc", "def", "dfg"]
#     index = int(input("Enter your index"))
#     print(my_list[index])
# except ValueError:
#     print("Your index must be numeric only")
# except IndexError:
#     print("Your index is out of range")

# try:
#     divide_by = int(input("Enter an integer number to divide (not zero)):"))
#     print(120 / divide_by)
# except ValueError:
#     print("You must enter a numeric value (not zero)")
# except ZeroDivisionError:
#     print("You can't divide by zero")

students_info_dictionary = {"327583828": "Kobi Levi", "358796939": "Avi Cohen"}

# Method 1
# try:
#     student_id = input("Enter student's id number:")
#
#     print(f"Student with id {student_id} is: {students_info_dictionary[student_id]}")
# except KeyError:
#     print("Student id doesn't exist")

# Method 2
# student_id = input("Enter student's id number:")
#
# print(
#     f"Student with id {student_id} is: {students_info_dictionary[student_id]}" if student_id in students_info_dictionary else "Student id doesn't exist")


# def get_user_age() -> int:
#     """
#     Function gets user's age
#     :raises ValueError This exception is thrown when the user's age is not numeric
#     :return: Getting user's age
#     """
#     try:
#         return int(input("Enter your age:"))
#     except ValueError:
#         raise ValueError("Your age can contain digits")
#
# #
# try:
#     print("Your age is:", get_user_age())
# except ValueError as v:
#     print(v)


# try:
#     grade = int(input("Enter your grade:"))
#
#     if grade < 0 or grade > 100:
#         raise ValueError
#
#     print(f"Your grade is:{grade}")
# except ValueError:
#     print("Wrong grade input. Must be a positive number between 0 and 100 only")


###############################################
# READING FROM A FILE
# from os.path import exists, isfile
#
# print(exists("test.txt") and isfile("test.txt"))
#
# try:
#     # r write קריאה
#     # a append הוספה
#     # w אם יש קופצ עוברת ומוחקת הכול ומסיפה מה את רושם   אם אין הקובץ יוסיף אותו\ תוכן
#     with open('t.txt', 'r') as f:  # a w
#         # print(f.read())  # ידפיס התוכן
        #
        # for line in f:
        #     print(line.rstrip())  # ידפיס שורה  בלי n\
        #
        # f.seek(0)  # חוזר להתחלה הקובץ
        # print(f.readlines())  # מדפיס מערך עם n\
        #
        # print([line.rstrip() for line in f.readlines()])  #מדפיס מערך בלי n\
        #
        # for line in reversed(f.readlines()):# בסדר הפוך
        #     print(line.rstrip())
        #
#         for line in f.readlines()[1:3]:#מדפיס מ שורה אחד עד 3 לא כולל
#             print(line.rstrip())
# except FileNotFoundError:
#     print("The specified file doesn't exist")
# except PermissionError:
#     print("You don't have permission to read from the file")
#
# # WRITING TO A FILE
# try:
#     with open('test.txt', 'w') as f:  # a
#         f.write("My amazing text")
# except PermissionError:
#     print("You don't have permission to read from the file")
#
#
###################################################
###################################################
##############################################
#################################



# for i in range(len(grades_list)):
#     print(grades_list[i])
#
# for grade in grades_list:
#     print(grade)
grades_list = [100, 97, 67, 55, 37, 97]
print(grades_list[1])  # 97
print(grades_list[1:4])  # [97, 67, 55]
print(grades_list[1:])  # [97, 67, 55, 37, 97]
print(grades_list[:4])  # [100, 97, 67, 55]
print(grades_list[-1], grades_list[5])  # 97 97
print(grades_list[1::2])  # [97, 55, 97]
print(grades_list[::-1])  # [97, 37, 55, 67, 97, 100]
print(len(grades_list))  # 6
print(97 in grades_list)  # True
#
# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
#
# print(matrix[1][1])

# random_numbers_list = []
# random_numbers_amount = 20
# bottom_random_value = 1
# top_random_value = 100
#
# for i in range(random_numbers_amount):
#     random_numbers_list.append(randint(bottom_random_value, top_random_value))
#
# print(random_numbers_list)

# random_numbers_list = [randint(bottom_random_value, top_random_value) for i in range(random_numbers_amount)]
# print(random_numbers_list)

# salaries_list = [12000, 30000, 10500, 23303]
# salaries_with_bonus = []
# smallest_valid_salary = 12000
#
# for salary in salaries_list:
#     if salary > smallest_valid_salary:
#         salaries_with_bonus.append(salary * 1.2)
#
# print(salaries_with_bonus)
#
# salaries_with_bonus = [salary * 1.2    for salary in salaries_list if
#                        salary > smallest_valid_salary]
# print(salaries_with_bonus)

# | & -
# print({1, 2, 3} & {2, 3, 4, 5})  # {2, 3}
# print({1, 2, 3} | {2, 3, 4, 5})  # {1, 2, 3, 4, 5}
# print({1, 2, 3} - {2, 3, 4, 5})  # {1}
#
# # Set functions
# print({1, 2, 3}.intersection({2, 3, 4, 5}))  # {2, 3}
# print({1, 2, 3}.union({2, 3, 4, 5}))  # {1, 2, 3, 4, 5}
# print({1, 2, 3}.symmetric_difference({2, 3, 4, 5}))  # {1, 4, 5}

# Dictionary
students_info_dictionary = {"357473727": 'Avi Cohen', "379695949": "Kobi Levi"}

# key_to_find = input("Enter a student's id:")
# print(students_info_dictionary[
#           key_to_find] if key_to_find in students_info_dictionary else "Student's id couldn't be found")

# Getting keys and values
# for key, value in students_info_dictionary.items():
#     print(key, ":", value)

# Getting values only
# for full_name in students_info_dictionary.values():
#     print(full_name)

for student_id in students_info_dictionary.keys():
    print(student_id)
#
# students_grades_list = {"357473728": [56, 67, 98, 34, 56, 100]}
# print(students_grades_list["357473728"][2])

# cars_list = {"1334556": {"car_type": "Ford", "manufacture_year": 1999, "color": "red"},
#              "9938792": {"car_type": "Hyundai", "manufacture_year": 2017, "color": "white"}
#              }

# print(cars_list["1334556"]["manufacture_year"])

#
# for car_license, car_info in cars_list.items():
#     print("Car's license number:", car_license)
#
#     for key, info in car_info.items():
#         print(key, ":", info)
#
#     print()

students_info_dictionary = {"357473727": 'Avi Cohen', "379695949": "Kobi Levi"}
students_info_dictionary["380907713"] = "Ariel Cohen"

print(students_info_dictionary["380907713"])


def display_message(message_to_display: str) -> None:
    """
    Function displays the given message
    :param message_to_display: Message to display
    :return: None
    """
    print(message_to_display)


display_message("Hello World!")
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

#

#



# try:
#     age = int(input("Enter your age"))
#     print("Your age is:", age)
# except ValueError:
#     print("Your age must contain digits only")

# try:
#     my_list = ["abc", "def", "dfg"]
#     index = int(input("Enter your index"))
#     print(my_list[index])
# except ValueError:
#     print("Your index must be numeric only")
# except IndexError:
#     print("Your index is out of range")

# try:
#     divide_by = int(input("Enter an integer number to divide (not zero)):"))
#     print(120 / divide_by)
# except ValueError:
#     print("You must enter a numeric value (not zero)")
# except ZeroDivisionError:
#     print("You can't divide by zero")

students_info_dictionary = {"327583828": "Kobi Levi", "358796939": "Avi Cohen"}


# def get_user_age() -> int:
#     """
#     Function gets user's age
#     :raises ValueError This exception is thrown when the user's age is not numeric
#     :return: Getting user's age
#     """
#     try:
#         return int(input("Enter your age:"))
#     except ValueError:
#         raise ValueError("Your age can contain digits")
#
#
# try:
#     print("Your age is:", get_user_age())
# except ValueError as v:
#     print(v)


try:
    grade = int(input("Enter your grade:"))

    if grade < 0 or grade > 100:
        raise ValueError

    print(f"Your grade is:{grade}")
except ValueError:
    print("Wrong grade input. Must be a positive number between 0 and 100 only")

