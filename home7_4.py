def common_elements():

    list_of_3 = {x for x in range(1, 101) if x % 3 == 0}
    list_of_5 = {x for x in range(1, 101) if x % 5 == 0}

    intersection = list_of_3 & list_of_5

    return intersection
assert common_elements() == {0, 75, 45, 15, 90, 60, 30}