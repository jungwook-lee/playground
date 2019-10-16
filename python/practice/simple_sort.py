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

def selection_sort(data):
    pass

def insertion_sort(data):
    pass


if __name__ == '__main__':
    sample = random.sample(range(100), 20)
    print(sample)
    bubble_sort(sample)
    print(sample)