class InvalidAgeError(Exception):
    def __init__(self, age):
        self.age = age

    def __str__(self):
        return f"Invalid age: {self.age}. Age must be a positive integer."


# Using the custom exception
age = -5
try:
    if age < 0:
        raise InvalidAgeError(age)
except InvalidAgeError as e:
    print(f"An error occurred: {e}")
