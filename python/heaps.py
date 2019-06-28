# Based on tutorial from https://towardsdatascience.com/data-structure-heap-23d4c78a6962
import random

def build_min_heap(array):
    """ Run min_heapify on all except the leafs"""
    for i in range((len(array)/2)-1, -1, -1):
        min_heapify(array, i)

def min_heapify(array, index):
    """ Keeps the min-heap property by swapping child if less"""
    if not array:
        return

    left = (2*index) + 1
    if len(array) > left and array[left] < array[index]:
        array[index], array[left] = array[left], array[index]
        min_heapify(array, left)

    right = (2*index) + 2
    if len(array) > right and array[right] < array[index]:
        array[index], array[right] = array[right], array[index]
        min_heapify(array, right)

def insert(array, data):
    if not array:
        return
    array.append(data)
    cur_i = len(array) - 1

    # Heapify the data
    while cur_i > 0:
        parent_i = (cur_i - 1) / 2
        min_heapify(array, parent_i)
        cur_i = parent_i

def extract_min(array):
    if not array:
        return

    # Make the last element the top of heap
    min_val = array[0]
    array[0] = array[-1]
    array.pop(-1)

    # heapify
    min_heapify(array, 0)
    return min_val


if __name__ == '__main__':
    # Build a min-heap
    # Make a random array
    arr = random.sample(range(100), 7)
    print(arr)

    build_min_heap(arr)
    print(arr)

    insert(arr, 6)
    print(arr)

    print(extract_min(arr))
    print(extract_min(arr))
    print(extract_min(arr))
    print(arr)
