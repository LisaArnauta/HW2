def three_biggest_int():
    first_list = [10, 11, 2, 3, 5, 8, 23, 11, 2, 5, 76, 43, 2, 32, 76, 3, 10, 0, 1]
    normal_list=list(set(first_list))
    maximum_list=[]
    for i in range(0,3):
        g = max(normal_list)
        maximum_list.append(g)
        normal_list.remove(g)
        print(maximum_list)
