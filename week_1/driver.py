#!/usr/bin/env python3

from quicksort_random_pivot import quicksort_random_pivot
from quicksort_perfect_pivot import quicksort_perfect_pivot
from random import shuffle, randint
from math import log2

def random_permutation(n):
  array = [i for i in range(n)]
  shuffle(array)
  return array

def random_array(n, min_value, max_value):
  return [randint(min_value, max_value) for i in range(n)]

def average_number_of_comparisons(n, array_generator):
  number_of_runs = max(10, int((10 ** 6) // (n * log2(n))))
  quicksort_rp_average = 0
  quicksort_pp_average = 0
  for _ in range(number_of_runs):
    array = array_generator(n)
    quicksort_rp_average += quicksort_random_pivot(array[:], 0, len(array))
    quicksort_pp_average += quicksort_perfect_pivot(array[:], 0, len(array), False)
  return n, int(n * log2(n)), number_of_runs, quicksort_rp_average // number_of_runs, quicksort_pp_average // number_of_runs

input_size = 10000

# Average number of comparisons for a permutation
print(average_number_of_comparisons(input_size, lambda n: random_permutation(n)))

# Average number of comparisons for a random array
print(average_number_of_comparisons(input_size, lambda n: random_array(n, 0, n)))

# Average number of comparisons for a random array with many duplicate values
print(average_number_of_comparisons(input_size, lambda n: random_array(n, 0, n // 100)))

# Average number of comparisons for a random array with few duplicate values
print(average_number_of_comparisons(input_size, lambda n: random_array(n, 0, n * 100)))
