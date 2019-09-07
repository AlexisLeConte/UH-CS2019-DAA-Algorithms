#!/usr/bin/env python3

def swap(array, a, b):
  """Swap the values at index a and index b of an array."""
  array[a], array[b] = array[b], array[a]

def quicksort_perfect_pivot(array, start, end, pivot_comparisons=False):
  """In-place quicksort with perfect pivot.
  array is the array to sort
  start is the index of the first element of the array to be sorted
  end is the index past the last element of the array to be sorted
  Returns the number of comparisons"""

  comparisons = 0

  # base case (single value)
  if end - 1 - start == 0:
    return 1

  # base case (empty array)
  if end - 1 - start < 0:
    return 0

  # select a pivot as close as possible to the perfect pivot
  perfect_pivot = (max(array[start:end]) + min(array[start:end])) // 2
  pivot_index, pivot_error = start, abs(perfect_pivot - array[start])
  for i in range(start + 1, end):
    if abs(perfect_pivot - array[i]) < pivot_error:
      pivot_index, pivot_error = i, abs(perfect_pivot - array[i])

  if pivot_comparisons:
    comparisons += 3 * (end - 1 - start)

  # place the selected pivot at the end of the array
  swap(array, pivot_index, end - 1)

  # assign the elements to a subarray
  cut = start
  for i in range(start, end - 1):
    # elements that are smaller than the pivot go into the first subarray
    if array[i] < array[end - 1]:
      swap(array, i, cut)
      cut += 1
    comparisons += 1

  # the pivot value should end the first subarray
  swap(array, cut, end - 1)
  
  # recursive quicksort call on both subarrays
  comparisons += quicksort_perfect_pivot(array, start, cut + 1)
  comparisons += quicksort_perfect_pivot(array, cut + 1, end)
  return comparisons
