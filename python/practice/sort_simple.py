""" Sorting Algorithm Practice """
import random

def bubble_sort(data):
    swap = False
    while True:
        # Go through each elements
        for i in range(len(data) - 1):
            if data[i] > data[i+1]:
                data[i], data[i+1] = data[i+1], data[i]
                swap = True
        # Continue until there are no swaps
        if not swap:
            return
        swap = False

def recursive_bubble_sort(data, i):
    # Base case
    if i == 0:
        return
    # Move the largest element to i
    for j in range(i):
        if data[j] > data[i]:
            data[i], data[j] = data[j], data[i]
    # Recursive case
    recursive_bubble_sort(data, i-1)

def selection_sort(data):
    for i in range(len(data) - 1):
        # use i to keep track of sorted section
        min_i = i
        for j in range(i, len(data)):
            # Find min value from unsorted section
            if data[j] < data[min_i]:
                min_i = j
        # Swap between min_j and i
        data[i], data[min_i] = data[min_i], data[i]

if __name__ == '__main__':
    sample = random.sample(range(100), 20)
    print(sample)
    bubble_sort(sample)
    print(sample)

    sample = random.sample(range(100), 20)
    print(sample)
    recursive_bubble_sort(sample, len(sample) - 1)
    print(sample)

    sample = random.sample(range(100), 20)
    print(sample)
    selection_sort(sample)
    print(sample)