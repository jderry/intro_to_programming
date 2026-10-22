# coding: utf-8
def count_chars(some_str: str) -> dict:
    # garbage filter
    # initialization
    count_dict = {}
    # implementation of the algorithm
    for symbol in some_str:
        try:
            count_dict[symbol] += 1
        except KeyError:
            count_dict[symbol] = 1
    return count_dict
