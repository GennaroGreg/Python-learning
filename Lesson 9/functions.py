def hello_python():
    print("Hello Python!")

hello_python()

def sum(num1, num2):
    if (type(num1) is not int or type(num2) is not int):
        return
    return num1 + num2

total = sum(2, 3)
print(total)

def multiple_items(*args):
    print(args)
    print(type(args))

multiple_items("Greg", "Percy", "Cody")

def mult_named_items(**kwargs): # kwargs = keyword args
    print(kwargs)
    print(type(kwargs))

mult_named_items(first = "Greg", last = "Gennaro")