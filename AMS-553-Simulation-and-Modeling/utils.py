import numpy as np
from random_variate_generator import RandomVariateGenerator

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

def generate_discrete_variates(values, generator = RandomVariateGenerator, count = 1, probabilities: list = None) -> list:
    if probabilities is not None and not np.isclose(sum(probabilities), 1.0):
        raise ValueError("Probabilities must sum to 1.")
    if probabilities is None:
        probabilities = np.full(count, [1/len(values)] * len(values))
    if not np.isclose(sum(probabilities), 1.0):
        raise ValueError("Probabilities must sum to 1.")
    look_up_table = generate_lookup_table(values, probabilities)
    results = [0] * count
    for i in range(count):
        index = int(generator.uniform() * len(look_up_table))
        results[i] = int(look_up_table[index])
    return results

def _normal_variates(generator, mean = 0.0, stddev = 1.0, count = 1):
    for _ in range(count):
        yield generator.normal(mean, stddev)

# TODO: Change this to the method that we learned in class
def normal_variables(generator, mean = 0.0, stddev = 1.0, count = 1, lower = -np.inf, upper = np.inf) -> list:
    variables = []
    for _ in range(count):
        while True:
            value = next(_normal_variates(generator, mean, stddev))
            if lower <= value <= upper:
                variables.append(value)
                break
    return variables