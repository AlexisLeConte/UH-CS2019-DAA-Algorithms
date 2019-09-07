from quicksort_random_pivot import quicksort_random_pivot
from quicksort_perfect_pivot import quicksort_perfect_pivot
from random import shuffle, randint

def random_permutation(size):
  array = [i for i in range(size)]
  shuffle(array)
  return array

def random_array(size, min_value, max_value):
  return [randint(min_value, max_value) for i in range(size)]

# random pivot quicksort usage example
array = random_array(1000, 0, 1000)
comparisons = quicksort_random_pivot(array, 0, len(array))
print(comparisons)

# perfect pivot quicksort usage example
array = random_permutation(1000)
comparisons = quicksort_perfect_pivot(array, 0, len(array), True)
print(comparisons)
