from math import ceil


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
