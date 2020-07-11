def lowest_int_index(input_list):
     input_list = [10, 11, 2, 3, 5, 8, 23,11, 2, 5, 76, 43, 2, 32, 76, 3, 10, 0, 1]
     minimum = min(input_list)
     index_of_minimum = input_list.index(minimum)
     print(index_of_minimum)