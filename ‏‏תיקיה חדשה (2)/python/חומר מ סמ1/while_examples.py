# integer_start_number = int(input("Enter an integer number to start with (between 0 and 10):"))
#
# while 0 <= integer_start_number <= 10:
#     print(integer_start_number)
#     integer_start_number += 1

ages_summary = 0
ages_amount = 0
smallest_age_value = 25
biggest_age_value = 65

while True:
    student_age = int(
        input("Enter your age (between " + str(smallest_age_value) + " and " + str(biggest_age_value) + "):"))

    if student_age == -1:
        break

    if smallest_age_value <= student_age <= biggest_age_value:
        ages_amount += 1
        ages_summary += student_age
    else:
        print("Error. Given ages must be between", smallest_age_value, "and", biggest_age_value)

if ages_amount > 0:
    print("Average of ages between", smallest_age_value, "and", biggest_age_value, "is:",
          ages_summary / ages_amount)
