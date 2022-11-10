#######################################################
#                  Exercise 3 Tests                   #
#                    Instructions                     #
#   1. Move this file the to exercise folder          #
#   2. Make sure there aren't any function calls      #
#      in your exercise files                         #
#   3. Run this file and check for errors or success  #
#######################################################


from ex3 import *
#import numpy as np

########################
#         A. 1         #
########################

# Test manually


########################
#         A. 2         #
########################

assert (calc_the_inner_product([1, 2, 3], [1, 2, 3]) == 14).all()
assert calc_the_inner_product([1, 2, 3], [10.5, -2, 0]) == 6.5
assert calc_the_inner_product([1, 2, 3], []) is None
assert calc_the_inner_product([0], [0]) == 0
assert calc_the_inner_product([-10], [-5]) == 50
assert calc_the_inner_product([], [1]) is None
assert calc_the_inner_product([], []) == 0


########################
#         A. 3         #
########################

"""assert (check_monotonic_sequence([1, 2, 3, 4, 5, 6, 7, 8])
        == [True, True, False, False])

assert (check_monotonic_sequence([1, 2, 2, 3])
        == [True, False, False, False])

assert (check_monotonic_sequence([1, 1, 1, 1])
        == [True, False, True, False])

assert (check_monotonic_sequence([3, 2, 1, 1])
        == [False, False, True, False])

assert (check_monotonic_sequence([7.5, 4, 3.141, 0.111])
        == [False, False, True, True])

assert (check_monotonic_sequence([1, 0, -1, 1])
        == [False, False, False, False])

assert (check_monotonic_sequence([])
        == [True, True, True, True])

assert (check_monotonic_sequence([100])
        == [True, True, True, True])

assert (check_monotonic_sequence([-10])
        == [True, True, True, True])

assert (check_monotonic_sequence([0])
        == [True, True, True, True])
"""

########################
#         A. 4         #
########################

"""bool_def = [True, True, False, False]
assert check_monotonic_sequence(check_monotonic_sequence_inverse(bool_def)) == bool_def

bool_def = [False, False, True, True]
assert check_monotonic_sequence(check_monotonic_sequence_inverse(bool_def)) == bool_def

bool_def = [True, False, True, False]
assert check_monotonic_sequence(check_monotonic_sequence_inverse(bool_def)) == bool_def

bool_def = [True, False, False, False]
assert check_monotonic_sequence(check_monotonic_sequence_inverse(bool_def)) == bool_def

bool_def = [False, False, True, False]
assert check_monotonic_sequence(check_monotonic_sequence_inverse(bool_def)) == bool_def

bool_def = [False, False, False, False]
assert check_monotonic_sequence(check_monotonic_sequence_inverse(bool_def)) == bool_def

bool_def = [True, True, True, True]
assert check_monotonic_sequence(check_monotonic_sequence_inverse(bool_def)) == bool_def
assert len(check_monotonic_sequence_inverse(bool_def)) <= 1


bool_def = [False, True, False, False]
assert check_monotonic_sequence_inverse(bool_def) is None

bool_def = [False, False, False, True]
assert check_monotonic_sequence_inverse(bool_def) is None"""




"""bool_def = [False, True, True, False]
assert check_monotonic_sequence_inverse(bool_def) is None

bool_def = [True, False, False, True]
assert check_monotonic_sequence_inverse(bool_def) is None
"""

########################
#         A. 5         #
########################

assert primes_generator(0) == []
assert primes_generator(1) == [2]
assert primes_generator(2) == [2, 3]
assert primes_generator(7) == [2, 3, 5, 7, 11, 13, 17]
assert primes_generator(50) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37,
                                41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83,
                                89, 97, 101, 103, 107, 109, 113, 127, 131,
                                137, 139, 149, 151, 157, 163, 167, 173, 179,
                                181, 191, 193, 197, 199, 211, 223, 227, 229]


########################
#         A. 6         #
########################

assert (vectors_list_sum([[1, 1], [1, 3]]) == [2, 4]).all()

assert (vectors_list_sum([[1, 1, 1], [1, 0, 0], [0, 0, 100]]) == [2, 1, 101]).all()

assert (vectors_list_sum([[1, 1, 1, 1, 1], [1, 1, 1, 1, 1]]) == [2, 2, 2, 2, 2]).all()


########################
#         A. 6         #
########################

assert (orthogonal_number([[1, 0, 0], [0, 1, 0], [0, 0, 1]]) == 3)

assert orthogonal_number([[0, 0], [1, 2], [10, 5]]) == 2

assert orthogonal_number([[1, 1, 1, 1],
                          [2, 1, 3, 3],
                          [0, 0, 100, 33],
                          [8, 8, 8, 1.5],
                          [9, 9, 9, 9]]) == 0

assert orthogonal_number([[0], [0], [0], [0]]) == 6

print("All tests passed")
