def data_types():
    my_list = [1,2,3]
    print(f"List: ", my_list)

    my_list.append(4)
    print(f"After adding", my_list)

    my_tuple = (8,9,10)
    print(f"Tuple: ", my_tuple)

    # tuples are immutable, so this will raise an AttributeError
    # my_tuple.append(11)  
    # print(f"After adding", my_tuple)  

    # duplicates got removed
    my_set = {4,5,6, 6, 5}
    print(f"Set: ", my_set)

    my_dict = {'a': 1, 'b': 2}
    print(f"Dictionary: ", my_dict)

data_types()