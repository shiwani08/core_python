def decorated_print(func):
    def wrapper():
        print("This is a decorated print function.")
        func()
        print("Finished running decorated function.")
    return wrapper

# my_function = decorated_print(my_function)
@decorated_print
def my_function():
    print("Inside my_function.")

my_function()
