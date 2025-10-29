def dict_example():

    my_dict = {'name': 'Bing', 'age': 21, 'marks': 85}
    print("Original dictionary:", my_dict)

    print("The keys are: ", list(my_dict.keys()))
    print("The values are: ", list(my_dict.values()))
    print("The items are: ", list(my_dict.items()))

    for keys, values in my_dict.items():
        print("Key:", type(keys))
        print("Value:", type(values))

dict_example()