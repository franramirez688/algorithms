#!/usr/bin/env python

"""
    Hash and order functions (compatible with python 2.7 and 3.5)
"""

from __future__ import print_function

import itertools

try:
    integer_types = (int, long)
except NameError:
    integer_types = int


letters = "acdefgilmnoprstuwy"


def hash(st):
    h = 7
    for i in range(len(st)):
        h = h * 37 + letters.index(st[i])
    return h


def order(h, st_len):
    """Resolve the sequence:
        hn - h0 * (37 ** n) = (37 ** (n-1)) * k0 + ... + 37 * k1 + kn-1   ->

        -> hn - h0 * (37 ** n) - (37 ** (n-1)) * k0 -  ... - 37 * k1 - kn-1 = 0


    such that the constants k0...kn-1 could have the values between [0 - 17] (global variable 'letters' length)

    :param h: number to get a correct word
    :param st_len: length of string to search
    :return: string with this length
    """
    letters_length = len(letters)
    st_len_is_valid = isinstance(st_len, int) and  0 < st_len <= len(letters)

    assert isinstance(h, integer_types), "h {} attribute must be an integer".format(h)
    assert st_len_is_valid, "st_len must be a positive integer value between [1, {}]".format(letters_length)

    letters_range = range(letters_length)
    indexes = []

    initial_sum_value = h - 7 * (37 ** st_len)
    upper_limit = [letters_range[-1]] * st_len
    lower_limit = [letters_range[0]] * st_len

    def get_total(*constants):
        """Given the sequence:
            hn - h0 * (37 ** n) - (37 ** (n-1)) * k0 -  ... - 37 * k1 - kn-1 = 0
        Get the valid result replacing the constants

        :param constants: list of arguments to check
        :return: result when it's resolved the mathematical formula
        :rtype: int
        """
        n = st_len - 1
        # Equivalent to:
        #   for i, constant in enumerate(constants[0]):
        #       c_sum += (37 ** (n - i)) * constant
        #   return (initial_sum_value - c_sum)
        return initial_sum_value - sum(itertools.starmap(lambda i, k: (37 ** (n - i)) * k, enumerate(constants[0])))

    def find_valid_index(index_pos):
        """Find recursively valid indexes

        :param index_pos: index position to check
        :return: None
        """
        if len(indexes) == st_len:
            return

        for k in letters_range:
            upper_limit[index_pos] = k
            lower_limit[index_pos] = k
            upper_total = get_total(upper_limit)
            lower_total = get_total(lower_limit)
            if lower_total >= 0 and upper_total <= 0:
                indexes.append(k)
                find_valid_index(index_pos + 1)
                break

    find_valid_index(0)

    if not indexes:
        raise Exception("It could not find any solution!")

    return ''.join([letters[i] for i in indexes])


if __name__ == '__main__':
    print(order(682498775709, 7))  # lampara
    print(order(18754844497, 6))  # pydoof
    print(order(hash('acdefgilmnoprstuwy'), 18))
    print(order(hash('aaaaaaaaaaaaaaaaaa'), 18))
    print(order(hash('yyyyyyyyyyyyyyyyyy'), 18))
    print(order(hash('ca'), 2))
    print(order(hash('a'), 1))
    print(order(hash('y'), 1))
