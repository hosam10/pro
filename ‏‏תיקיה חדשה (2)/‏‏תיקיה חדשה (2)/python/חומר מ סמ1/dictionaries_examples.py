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
