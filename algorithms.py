#!/usr/bin/env python

def find_a_sequence_inside_another_sequence(seq, seq_to_find):
    """Check if a sequence exist in another sequence

       Example:
           seq = [1,2,4,5,6,2,3,1,2,3,4]
           seq_to_find = [4,5,6]

           find_a_sequence_inside_another_sequence(seq, seq_to_find)
           >> True

        :type seq: list
        :type seq_to_find: list
        :rtype: boolean
    """
    if len(seq) < len(seq_to_find):
        return False

    pos = 0
    for item in seq:
        if seq_to_find[pos] == item:
            pos += 1
            if pos == len(seq_to_find):
                return True
            continue
        pos = 0
    return False


if __name__ == '__main__':
    print(find_a_sequence_inside_another_sequence([1,4,3,5,1,2,3,4],
                                                  [1,2,3]))
    print(find_a_sequence_inside_another_sequence([1,5,1,2],
                                                  [1,2,3]))
    print(find_a_sequence_inside_another_sequence([1,2],
                                                  [1,2,3]))
