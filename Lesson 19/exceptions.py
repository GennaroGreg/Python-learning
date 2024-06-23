class CustomError(Exception):
    pass

x = 2
try:
    # print(x / 0)
    # if not type(x) is str:
    #     raise TypeError("Only strings are allowed.")
    raise CustomError("This is a custom exception!")
except NameError:
    print("NameError encountered!")
except ZeroDivisionError:
    print("You can't divide by zero!")
except Exception as error:
    print(error)
else:
    print('No errors!')
finally:
    print("This code triggers with or without errors.")

