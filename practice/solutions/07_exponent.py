def exponent():
    base = int(input("Enter the base number: "))
    exponent = int(input("Enter the exponent number: "))

    try:
        result = base ** exponent
        print("The result is", result)
        
    except Exception as e:
        print("Error:", e)

exponent()