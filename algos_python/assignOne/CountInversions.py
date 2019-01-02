def split_list(my_list):
    """

    :param my_list: list of integers to be split into half
    :return: tuple of left half and right half
    """
    half = int(len(my_list) / 2)
    fhalf = my_list[:half + 1]
    shalf = my_list[half:]

    return fhalf, shalf


def count_merge(fhalf_tup, shalf_tup):
    """

    :param fhalf_tup: (ordered list of integers, inversions from ordering)
    :param shalf_tup: (ordered list of integers, inversions from ordering)
    :return: tuple of merged list and inversions
    """

    fhalf = fhalf_tup[0]
    shalf = shalf_tup[0]
    inv = fhalf_tup[1] + shalf_tup[1]
    F = len(fhalf)
    S = len(shalf)
    merged_list = []
    f: int = 0
    s = 0

    while f < F and s < S:
        f_elem = fhalf[f]
        s_elem = shalf[s]
        if f_elem < s_elem:
            merged_list.append(f_elem)
            f += 1
        else:
            merged_list.append(s_elem)
            s += 1
            inv += (F - f)

    while f < F:
        merged_list.append(fhalf[f])
        f += 1

    while s < S:
        merged_list.append(shalf[s])
        s += 1

    return merged_list, inv


def my_sort(my_list):
    """

    :param my_list: list to be sorted
    :return: tuple of (sorted list, number of inversions)
    """
    if len(my_list) == 1:
        return my_list, 0
    else:
        fhalf, shalf = split_list(my_list)
        fhalf_sort = my_sort(fhalf)
        shalf_sort = my_sort(shalf)
        return count_merge(fhalf_sort, shalf_sort)
