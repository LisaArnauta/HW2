def find_common_keys(dict1, dict2):
    dict_1 = dict(input('write your first dict here: '))
    dict_2 = dict(input('write your second dict here: '))
    sim = list(dict_1.keys() & dict_2.keys())
    print(sim)
