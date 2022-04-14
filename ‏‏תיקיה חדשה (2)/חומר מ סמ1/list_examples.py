grades_list = [100, 97, 67, 55, 37, 97]

for i in range(len(grades_list)):
    print(grades_list[i])

for grade in grades_list:
    print(grade)

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

grades = [67, 78, 98, 23, 45, 56, 45]
# grades.append(99)  # Adding a new element to the end of the list
# print(grades)  # [67, 78, 98, 23, 45, 56, 45, 99]

# print(grades.index(45))  # 4 - displaying an index of the first element which equals to 45
# print(grades.count(45))  # Displaying an amount of elements that that their value is equal to 45

# grades.remove(45)  # Removing the first element which value is equal to 45

# removed_grade = grades.pop(1)
# print(removed_grade)

# print(grades.pop())  # If we haven't defined an index, removing the last element