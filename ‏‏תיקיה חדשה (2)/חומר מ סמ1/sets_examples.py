fruits_set = {"apple", "banana", "cherry"}
# print(fruits_set)
#
# print(len(fruits_set))
# print(type(fruits_set))
#
# numbers_list = [1, 3, 2, 1, 57, 5, 9, 7, 3, 2]
# print(set(numbers_list))
#
# for fruit in fruits_set:
#     print(fruit)

# print("banana" in fruits_set)
# fruits_set.add("orange")
# print(fruits_set)

# tropical_fruits_set = {"pineapple", "mango", "papaya"}
# fruits_set.update(tropical_fruits_set)

# another_fruits_list = ["kiwi", "orange", "kiwi"]
# fruits_set.update(another_fruits_list)

# fruits_set.remove("orange")

# fruits_set.discard("orange")
# print(fruits_set)

# max([1, 422, 22, 77, 9])
# numbers_set = {1, 422, 22, 77, 9}
# print(sorted(numbers_set))
numbers_set = {1, 422, 22, 77, 9}
print(sorted(numbers_set, reverse=True))


# | & -
print({1, 2, 3} & {2, 3, 4, 5})  # {2, 3}
print({1, 2, 3} | {2, 3, 4, 5})  # {1, 2, 3, 4, 5}
print({1, 2, 3} - {2, 3, 4, 5})  # {1}

# Set functions
print({1, 2, 3}.intersection({2, 3, 4, 5}))  # {2, 3}
print({1, 2, 3}.union({2, 3, 4, 5}))  # {1, 2, 3, 4, 5}
print({1, 2, 3}.symmetric_difference({2, 3, 4, 5}))  # {1, 4, 5}

first_set = {1, 2, 3}
first_set.intersection_update({2, 3, 4, 5})
print(first_set)
