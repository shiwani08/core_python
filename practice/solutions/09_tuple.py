def tuples():
    my_tuple = (1, 2, 3, 4, 5)

    print("Original tuple:", my_tuple)

    try:
        my_tuple[0] = 10
    except TypeError as e:
        print("Error:", e)  

tuples()