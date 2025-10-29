def list_functions():

    try:
        my_list = [5, 2, 9, 1, 5, 6]
        print("Original List:", my_list)

        my_list.append(10)
        print("After append(10):", my_list)

        my_list.extend([20, 25])
        print("After extend([20, 25]):", my_list)

        my_list.remove(5)
        print("After remove(5):", my_list)

        my_list.sort()
        print("After sort():", my_list)

        print("Index of 9:", my_list.index(9))  

        my_list.reverse()
        print("After reverse():", my_list)  

        my_list.insert(2, 15)
        print("After insert(2, 15):", my_list)

        my_list.pop()
        print("After pop():", my_list)

        my_list.count(5)
        print("Count of 5:", my_list.count(5))

    except Exception as e:
        print("Error:", e)

list_functions()