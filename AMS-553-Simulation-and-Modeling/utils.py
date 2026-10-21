import numpy as np
from random_variate_generator import UniformRandomVariableGenerator

def max_decimal_digits(arr):
    s_arr = arr.astype(str)
    s_arr = np.char.rstrip(s_arr, '0')
    dots = np.char.find(s_arr, '.')
    lengths = np.char.str_len(s_arr)
    decimal_counts = np.where(dots != -1, lengths - dots - 1, 0)
    return np.max(decimal_counts)

def generate_lookup_table(values, probabilities):
    multiplier = max_decimal_digits(np.array(probabilities))
    repeats = (np.array(probabilities) *  ((10 ** multiplier))).astype(int)
    look_up_table = np.repeat(values, repeats=repeats)
    return look_up_table

def generate_discrete_variates(values, probabilities, count, urv):
    look_up_table = generate_lookup_table(values, probabilities)
    for _ in range(count):
        index = int(urv.next_uniform() * len(look_up_table))
        yield int(look_up_table[index])