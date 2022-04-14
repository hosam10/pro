def checking_num_in_file(num: int, text: str):
    try:
        with open(text, 'a')as  f:
            for i in range(10):
                 f.write(str(i))

    except FileNotFoundError:
        print("your file not excist")
    except PermissionError:
        print("You don't have permission to read from the file")


# input_file
# try:
num = int(input("enter your number"))
checking_num_in_file(num, "t11.txt")

#     print(checking_num_in_file(num, "t.txt"))
# except FileExistsError as s:
#     print(s)
# except PermissionError as p:
#     print(p)
