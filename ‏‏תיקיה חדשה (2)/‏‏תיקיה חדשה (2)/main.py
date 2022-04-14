from testfunctions import*


try:
    use_program()
except TypeError as i:
    print (i)
except ValueError as v:
    print(v)
