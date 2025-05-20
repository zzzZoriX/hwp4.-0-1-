def find_min(list: list[int]) -> int:
    if(len(list) <= 0):
        raise ValueError('список нулевой длины')

    min: int = list[0]
    for i in range(1, len(list)):
        if(min > list[i]): min = list[i]

    return min

def find_avg(list: list[int]) -> float:
    if(len(list) <= 0):
        raise ValueError('список нулевой длины')

    return sum(list) / len(list)

def find_second_max(list: list[int]) -> int:
    if(len(list) <= 0):
        raise ValueError('список нулевой длины')

    list.remove(max(list))
    return max(list)

def find_sum_of_even_nums(list: list[int]) -> int:
    if(len(list) <= 0):
        raise ValueError('список нулевой длины')

    return sum([el for el in list if el % 2 == 0])

def is_monotone(list: list[int]) -> bool:
    if(len(list) <= 0):
        raise ValueError('список нулевой длины')

    inc: bool = True
    dec: bool = True

    for i in range(1, len(list)):
        if(list[i - 1] >= list[i]): inc = False
        elif(list[i - 1] <= list[i]): dec = False

    return inc or dec