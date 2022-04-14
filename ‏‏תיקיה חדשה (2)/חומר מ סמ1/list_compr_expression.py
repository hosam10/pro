# list comprehension python
# salaries_list = [12300, 25000, 10200, 21500]
# salaries_bonus = 1.15
# min_valid_salary = 12500
#
# salaries_with_bonus = []
#
# for salary in salaries_list:
#     if salary > min_valid_salary:
#         salaries_with_bonus.append(round(salary * salaries_bonus))
#
# print(salaries_with_bonus)
#
# salaries_with_bonus = [round(salary * salaries_bonus) for salary in salaries_list if salary > min_valid_salary]
# print(salaries_with_bonus)

grades_list = [53, 67, 89, 91, 100, 13, 100]
grade_factor = 1.15
pass_grade = 56
highest_grade = 100

grades_with_factor = []

for grade in grades_list:
    if pass_grade <= grade <= highest_grade:
        grades_with_factor.append(
            round(grade * grade_factor) if grade * grade_factor <= highest_grade else highest_grade)

print(grades_with_factor)

grades_with_factor = [round(grade * grade_factor) if grade * grade_factor <= highest_grade else highest_grade for grade
                      in
                      grades_list if pass_grade <= grade <= highest_grade]

print(grades_with_factor)
