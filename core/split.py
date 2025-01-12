from math import ceil


def split_in_six(long_list):
    cursor = ceil(len(long_list) / 6)

    return (
        long_list[:cursor],
        long_list[cursor : 2 * cursor],
        long_list[2 * cursor : 3 * cursor],
        long_list[3 * cursor : 4 * cursor],
        long_list[4 * cursor : 5 * cursor],
        long_list[5 * cursor :],
    )


def split_in_three(long_list):
    cursor = ceil(len(long_list) / 3)

    return (
        long_list[:cursor],
        long_list[cursor : 2 * cursor],
        long_list[2 * cursor :],
    )


def split_in_two(long_list):
    cursor = ceil(len(long_list) / 2)

    return long_list[:cursor], long_list[cursor:]
