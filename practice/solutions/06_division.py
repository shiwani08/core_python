def div_floor():
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter another number: "))

    try:
        print(f"{type(num1)} {type(num2)}")

        division = num1 / num2 
        print("The result is", division)

        floor_division = num1 // num2   
        print("The floor result is", floor_division)

    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")

div_floor()