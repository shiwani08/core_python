def part_1():

    print ("\nPart 1:")
    deci = 54.87
    print (f"Float: {deci}")
    print (type(deci))

    deci = int(deci)
    print (f"Converted Float to Int: {deci}")
    print (type(deci))

    converted_str = str(deci)
    print (f"Converted Int to String: {converted_str}")
    print (type(converted_str))

    num = "78"
    print (f"String: {num}")
    print (type(num))

    num = int(num)
    print (f"Converted String to Int: {num}")
    print (type(num))

def part_2():

    print ("\nPart 2:")
    str_num = "123.45"
    print (f"String: {str_num}")
    print (type(str_num))
    str_num = float(str_num)
    print (f"Converted String to Float: {str_num}")
    print (type(str_num))
    str_num = int(str_num)
    print (f"Converted Float to Int: {str_num}")
    print (type(str_num))

def part_3():

    print ("\nPart 3:")
    nums = [1, 2, 3]
    print (f"List: {nums}")
    print (type(nums))

    #  mapping or looping is done 
    str_nums = ','.join(map(str, nums))
    print (f"Converted List to String: {str_nums}")
    print (type(str_nums))  

part_1()
part_2()
part_3()